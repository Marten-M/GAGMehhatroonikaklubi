"""Robot arm class file."""
from typing import Tuple

from ....lib.mathfunctions import get_angle_between_triangle_sides, get_area_heron, arcsin, arccos

from ...lib.motors.stepper import Stepper
from ...lib.motors.servo import Servo

from .electromagnet import ElectroMagnet


class RobotArm(object):
    def __init__(self, first_arm_length: float, second_arm_length: float, starting_height: float, stepper: Stepper, first_arm_servo: Servo, first_servo_zero_position_offset_angle: int, second_arm_servo: Servo, second_servo_zero_position_offset_angle: int, electromagnet: ElectroMagnet):
        """
        Initialize class.

        :param first_arm_length: length of first arm in cm
        :param second_arm_length: length of second arm in cm
        :param starting_height: height of the base of the first arm in cm
        :param stepper: Stepper class of the stepper motor that controls the arm
        :param first_arm_servo: Servo class of the servo motor controlling the first arm
        :param first_servo_zero_position_offset_angle: angle that the first arm is offset from right angle from its zero position
        :param second_arm_servo: Servo class of the servo motor controlling the second arm
        :param second_servo_zero_position_offset_angle: angle that the second arm is offset from right angle from its -90degrees position
        :param electromagnet: ElectroMagnet class of the electormagnet attached to the robot arm
        """
        self.first_arm_length = first_arm_length
        self.second_arm_length = second_arm_length
        self.height = starting_height

        self.stepper = stepper
        self.cur_angle = 0

        self.first_arm_servo = first_arm_servo
        self.second_arm_servo = second_arm_servo

        self.electromagnet = electromagnet

        self.first_servo_zero_position_offset_angle = first_servo_zero_position_offset_angle
        self.second_servo_zero_position_offset_angle = second_servo_zero_position_offset_angle

    def get_servo_angles(self, distance_from_arm: float, height: float) -> Tuple[int, int]:
        """
        Get angles the servos should go under to reach desired distance.

        :param distance_from_arm: distance to target
        :param height: height of target spot

        :return: angle of first and second servo in the form (first_servo_angle, second_servo_angle)
        """
        third_side = ((self.height - height) ** 2 + distance_from_arm ** 2) ** 0.5
        if height <= self.height:
            a = self.first_servo_zero_position_offset_angle + 90 + (180 - (arccos((self.second_arm_length ** 2 - self.first_arm_length ** 2 - third_side ** 2) / (-2 * self.first_arm_length * third_side)) + arcsin(distance_from_arm / third_side)))
        else:
            a = self.first_servo_zero_position_offset_angle + 90 + (180 - (arccos((self.second_arm_length ** 2 - self.first_arm_length ** 2 - third_side ** 2) / (-2 * self.first_arm_length * third_side)) + 90 + arcsin((height - self.height) / third_side)))
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

    def move_arm_to_position(self, target_stepper_angle: float, target_dist: float, target_height: float):
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
        self.second_arm_servo.set_angle(b)
        self.first_arm_servo.set_angle(a)
        
