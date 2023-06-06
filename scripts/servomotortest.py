"""Script for testing the servo motors."""

import os
import sys

source_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, source_path)

from src.classes.lib.motors.servo import Servo
from src.constants import *

from time import sleep


if __name__ == "__main__":
    servo1 = Servo(FIRST_SERVO_PIN, SERVO_MIN_POSITION_PULSE_WIDTH_MS, SERVO_MAX_POSITION_PULSE_WIDTH_MS)
    servo2 = Servo(SECOND_SERVO_PIN, SERVO_MIN_POSITION_PULSE_WIDTH_MS, SERVO_MAX_POSITION_PULSE_WIDTH_MS)
    sleep(2)
    while True:
        servo1.set_angle(90)
        sleep(2)
        servo1.set_angle(120)
        sleep(2)
        servo2.set_angle(120)
        sleep(2)
        servo2.set_angle(90)
        sleep(2)
