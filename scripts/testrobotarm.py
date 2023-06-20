"""Script for testing the robot arm."""

import os
import sys

source_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, source_path)

from gpiozero import Button

from src.constants import *
from src.classes.chessrobot.robotarm.robotarm import RobotArm
from src.classes.lib.motors.servowithgeartrain import GearTrainServo
from src.classes.lib.motors.stepper import Stepper
from src.classes.chessrobot.robotarm.electromagnet import ElectroMagnet

from time import sleep

if __name__ == "__main__":
    first_servo = GearTrainServo(FIRST_SERVO_PIN, SERVO_MIN_POSITION_PULSE_WIDTH_MS, SERVO_MAX_POSITION_PULSE_WIDTH_MS, SERVO_PULSE_FRAME_WIDTH_MS, FIRST_ARM_GEAR_RATIO, FIRST_ARM_ZERO_POSITION_OFFSET_ANGLE_DEGREES, True, FIRST_ARM_MINIMUM_ANGLE_DEGREES, FIRST_ARM_MAXIMUM_ANGLE_DEGREES)
    second_servo = GearTrainServo(SECOND_SERVO_PIN, SERVO_MIN_POSITION_PULSE_WIDTH_MS, SERVO_MAX_POSITION_PULSE_WIDTH_MS, SERVO_PULSE_FRAME_WIDTH_MS, SECOND_ARM_GEAR_RATIO, SECOND_ARM_ZERO_POSITION_OFFSET_ANGLE_DEGREES, False, SECOND_ARM_MINIMUM_ANGLE_DEGREES, SECOND_ARM_MAXIMUM_ANGLE_DEGREES)
    
    stepper = Stepper(STEPPER_STEP_PIN, STEPPER_DIRECTION_PIN, STEPPER_STEP_DEGREES)
    # Zero the stepper motor
    detector = Button(STEPPER_ZERO_POSITION_DETECT_PIN)
    while not detector.is_pressed:
        stepper.rotate_steps(1)

    magnet = ElectroMagnet(ELECTROMAGNET_PULL_PIN, ELECTROMAGNET_PUSH_PIN, MAGNET_PULL_DISTANCE_CM, ELECTROMAGNET_HEIGHT_CM)

    arm = RobotArm(FIRST_ARM_LENGTH_CM, SECOND_ARM_LENGTH_CM, ARM_HEIGHT_CM, stepper, first_servo, second_servo, magnet)

    arm.move_arm_to_position(30, 50, 15)
    sleep(4)
    arm.move_arm_to_position(30, 50, 15)
