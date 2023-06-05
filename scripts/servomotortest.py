"""Script for testing the servo motors."""

import os
import sys

source_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, source_path)

from src.classes.lib.motors.servo import Servo
from src.constants import *

from time import sleep

if __name__ == "__main__":
    servo1 = Servo(FIRST_SERVO_PIN)
    servo2 = Servo(SECOND_SERVO_PIN)
    while True:
        servo1.set_angle(0)
        sleep(2)
        servo1.set_angle(180)
        sleep(2)
        servo2.set_angle(0)
        sleep(2)
        servo2.cur_angle(180)
        sleep(2)
