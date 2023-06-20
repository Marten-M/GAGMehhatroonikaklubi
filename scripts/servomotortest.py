"""Script for testing the servo motors."""

import os
import sys

source_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, source_path)

from src.classes.lib.motors.servowithgeartrain import GearTrainServo
from src.constants import *

from time import sleep


if __name__ == "__main__":
    servo1 = GearTrainServo(FIRST_SERVO_PIN, SERVO_MIN_POSITION_PULSE_WIDTH_MS, SERVO_MAX_POSITION_PULSE_WIDTH_MS, SERVO_PULSE_FRAME_WIDTH_MS, FIRST_ARM_GEAR_RATIO, FIRST_ARM_ZERO_POSITION_OFFSET_ANGLE_DEGREES, True, FIRST_ARM_MINIMUM_ANGLE_DEGREES, FIRST_ARM_MAXIMUM_ANGLE_DEGREES)
    servo2 = GearTrainServo(SECOND_SERVO_PIN, SERVO_MIN_POSITION_PULSE_WIDTH_MS, SERVO_MAX_POSITION_PULSE_WIDTH_MS, SERVO_PULSE_FRAME_WIDTH_MS, SECOND_ARM_GEAR_RATIO, SECOND_ARM_ZERO_POSITION_OFFSET_ANGLE_DEGREES, False, SECOND_ARM_MINIMUM_ANGLE_DEGREES, SECOND_ARM_MAXIMUM_ANGLE_DEGREES)
    sleep(2)
    while True:
        nums = list(map(int, input().split()))
        servo1.set_output_angle(nums[0])
        servo2.set_output_angle(nums[1])

