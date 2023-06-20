"""Script to test the LED script"""

import os
import sys

source_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, source_path)

from src.constants import *
from src.classes.lib.ledstrip import LEDStrip

from time import sleep

if __name__ == "__main__":
    strip = LEDStrip(MAIN_BOARD_LED_PIN, MAIN_BOARD_PIXEL_COUNT)
    strip.set_strip_color((255, 255, 255))
    strip.show_strip()