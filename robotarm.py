"""Robot arm class file."""
from typing import Tuple
from functions import get_angle_between_triangle_sides, get_area_heron, arcsin


class RobotArm(object):
    def __init__(self, first_arm_length: float, second_arm_length: float, starting_height: float, stepper_motor_step: float) -> None:
        """
        Initialize class.

        :param first_arm_length: length of first arm in cm
        :param second_arm_length: length of second arm in cm
        :param starting_height: height of the base of the first arm in cm
        :param stepper_motor_step: how many degrees the stepper motor moves with 1 step
        """
        self.first_arm = first_arm_length
        self.second_arm = second_arm_length
        self.height = starting_height

        self.step = 1.6
        self.cur_angle = 90

    def get_servo_angles(self, distance_from_arm: float, button_height: float) -> Tuple[float, float]:
        """
        Get angles the servos should go under to reach desired distance.

        :param distance_from_arm: distance to target square's center point in cm
        :param button_height: height of button in cm

        :return: angle of first and second servo in the form (first_servo_angle, second_servo_angle)
        """
        third_side = ((self.height - button_height) ** 2 + distance_from_arm ** 2) ** 0.5
        area = get_area_heron(self.first_arm, self.second_arm, third_side)

        a = arcsin(distance_from_arm / third_side) + get_angle_between_triangle_sides(area, self.first_arm, third_side)
        b = get_angle_between_triangle_sides(area, self.first_arm, self.second_arm)

        return (a, b)
    
    def get_stepper_steps(target_angle: float) -> int:
        """
        Get how many steps the stepper motor should do to reach desired robot arm angle to board.
        
        Steps are negative if the motor should rotate counter-clockwise and positive if clockwise.

        :param target_angle: desired angle to reach in degrees

        :return: integer representing number of steps the stepper motor has to take
        """
        


