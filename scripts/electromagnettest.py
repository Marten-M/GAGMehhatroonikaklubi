"""Script for testing whether electromagnet works."""

import os
import sys

source_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, source_path)

from src.constants import *
from src.classes.chessrobot.robotarm.electromagnet import ElectroMagnet

from time import sleep

if __name__ == "__main__":
    magnet = ElectroMagnet(ELECTROMAGNET_PULL_PIN, ELECTROMAGNET_PUSH_PIN, MAGNET_PULL_DISTANCE_CM)
    while True:
        magnet.pull()
        sleep(3)
        magnet.disable()
        sleep(2)