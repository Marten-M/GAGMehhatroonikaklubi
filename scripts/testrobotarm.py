"""Script for testing the robot arm."""

import os
import sys

source_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, source_path)

from gpiozero import Button

from src.constants import *
from src.classes.chessrobot.robotarm.robotarm import RobotArm
from src.classes.lib.motors.servo import Servo
from src.classes.lib.motors.stepper import Stepper
from src.classes.chessrobot.robotarm.electromagnet import ElectroMagnet

from time import sleep

if __name__ == "__main__":
    first_servo = Servo(FIRST_SERVO_PIN, SERVO_MIN_POSITION_PULSE_WIDTH_MS, SERVO_MAX_POSITION_PULSE_WIDTH_MS)
    second_servo = Servo(SECOND_SERVO_PIN, SERVO_MIN_POSITION_PULSE_WIDTH_MS, SERVO_MAX_POSITION_PULSE_WIDTH_MS)
    
    stepper = Stepper(STEPPER_STEP_PIN, STEPPER_DIRECTION_PIN, STEPPER_STEP_DEGREES)
    # Zero the stepper motor
    detector = Button(STEPPER_ZERO_POSITION_DETECT_PIN)
    while not detector.is_pressed:
        stepper.rotate_steps(1)

    magnet = ElectroMagnet(ELECTROMAGNET_PULL_PIN, ELECTROMAGNET_PUSH_PIN, MAGNET_PULL_DISTANCE_CM)

    arm = RobotArm(FIRST_ARM_LENGTH_CM, SECOND_ARM_LENGTH_CM, ARM_HEIGHT_CM, stepper, first_servo, FIRST_ARM_ZERO_POSITION_OFFSET_ANGLE_DEGREES, second_servo, SECOND_ARM_ZERO_POSITION_OFFSET_ANGLE_DEGREES, magnet)

    arm.move_arm_to_position(-90, 30, 10)
