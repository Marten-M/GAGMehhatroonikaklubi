"""Robot arm class file."""
from typing import Tuple
import time
from ....lib.mathfunctions import arcsin, arccos

from ...lib.motors.stepper import Stepper
from ...lib.motors.servowithgeartrain import GearTrainServo
from .electromagnet import ElectroMagnet


class RobotArm(object):
    def __init__(self, first_arm_length: float, second_arm_length: float, starting_height: float, stepper: Stepper, first_arm_servo: GearTrainServo, second_arm_servo: GearTrainServo, electromagnet: ElectroMagnet):
        """
        Initialize class.

        :param first_arm_length: length of first arm in cm
        :param second_arm_length: length of second arm in cm
        :param starting_height: height of the base of the first arm in cm
        :param stepper: Stepper class of the stepper motor that controls the arm
        :param first_arm_servo: GearTrainServo class of the servo motor controlling the first arm
        :param second_arm_servo: GearTrainServo class of the servo motor controlling the second arm
        :param electromagnet: ElectroMagnet class of the electormagnet attached to the robot arm
        """
        self.first_arm_length = first_arm_length
        self.second_arm_length = second_arm_length
        self.height = starting_height

        self.stepper = stepper
        self.cur_angle = 0

        self.first_arm_servo = first_arm_servo
        self.second_arm_servo = second_arm_servo

        self.cur_dist = 0
        self.cur_height = 0

        self.electromagnet = electromagnet

    def get_servo_angles(self, distance_from_arm: float, height: float) -> Tuple[int, int]:
        """
        Get angles the servos should go under to reach desired distance.

        :param distance_from_arm: distance to target
        :param height: height of target spot

        :return: angle of first and second servo in the form (first_servo_angle, second_servo_angle)
        """
        third_side = ((self.height - height) ** 2 + distance_from_arm ** 2) ** 0.5
        if height <= self.height:
            a = 90 + (180 - (arccos((self.second_arm_length ** 2 - self.first_arm_length ** 2 - third_side ** 2) / (-2 * self.first_arm_length * third_side)) + arcsin(distance_from_arm / third_side)))
        else:
            a = 90 + (180 - (arccos((self.second_arm_length ** 2 - self.first_arm_length ** 2 - third_side ** 2) / (-2 * self.first_arm_length * third_side)) + 90 + arcsin((height - self.height) / third_side)))
        b = self.second_servo_zero_position_offset_angle + 180 - arccos((third_side ** 2 - self.first_arm_length ** 2 - self.second_arm_length ** 2) / (-2 * self.first_arm_length * self.second_arm_length))

        return (int(a), int(b))

    def get_stepper_steps(self, target_angle: float) -> int:
        """
        Get how many steps the stepper motor should do to reach desired robot arm angle to board.
        
        Steps are negative if the motor should rotate counter-clockwise and positive if clockwise.

        :param target_angle: desired angle to reach in degrees

        :return: integer representing number of steps the stepper motor has to take
        """
        steps = (self.cur_angle - target_angle) / self.stepper.step

        if int(abs(steps) * 10) % 10 >= 5: # Get the tenths
            steps = int(steps) + 1 if steps >= 0 else int(steps) - 1
        else:
            steps = int(steps)

        return steps

    def move_arm_to_position(self, target_stepper_angle: float, target_dist: float, target_height: float, order=True):
        """
        Move arm to given position.

        :param target_stepper_angle: desired angle that stepper should take
        :param target_dist: target distance the arm should reach
        :param target_height: target height the arm should reach
        """
        steps = self.get_stepper_steps(target_stepper_angle)
        print(steps)
        self.stepper.rotate_steps(steps)
        self.cur_angle += -steps * self.stepper.step

        a, b = self.get_servo_angles(target_dist, target_height + self.electromagnet.height)
        print(f"Angles: {a}, {b}")

        if order:
            self.first_arm_servo.set_output_angle(a)
            self.second_arm_servo.set_output_angle(b)
        else:
            self.second_arm_servo.set_output_angle(b)
            self.first_arm_servo.set_output_angle(a)
        self.cur_dist = target_dist
        self.cur_height = target_height

    def move_arm_vertically(self, distance: float):
        """
        Move the robot arm straight up or down a given distance.

        :param distance: distance to move the arm in cm. Should be positive if arm should be moved down and negative if up
        """
        if distance >= 0:
            for target in range(self.cur_height, self.cur_height + distance, 0.5):
                self.move_arm_to_position(self.cur_angle, self.cur_dist, target)
        else:
            for target in range(self.cur_height + distance, self.cur_height, -0.5):
                self.move_arm_to_position(self.cur_angle, self.cur_dist, target)

    def zero_steps(self):
        self.stepper.zero_step()
        self.cur_angle = 0
