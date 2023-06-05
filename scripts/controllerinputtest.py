"""File for testing controller input functions."""

import os
import sys

source_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, source_path)

from src.classes.chessrobot.controller.controller import Controller
from src.constants import *

if __name__ == "__main__":
    controller = Controller(CONTROLLER_UP_PIN, CONTROLLER_DOWN_PIN, CONTROLLER_LEFT_PIN, CONTROLLER_RIGHT_PIN, CONTROLLER_BACK_PIN, CONTROLLER_ENTER_PIN)
    while True:
        inpt = controller.get_input()
        print(inpt)
