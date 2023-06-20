"""Script for testing the stepper motor."""

import os
import sys

source_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, source_path)

from src.classes.lib.motors.stepper import Stepper
from src.constants import *

from time import sleep

if __name__ == "__main__":
    stepper = Stepper(STEPPER_STEP_PIN, STEPPER_DIRECTION_PIN, STEPPER_STEP_DEGREES)
    stepper.rotate_steps(-4800)
