"""Script for testing LCD screen."""

import os
import sys

source_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, source_path)

from src.constants import *
from src.classes.lib.lcdscreen import LCDScreen

from time import sleep


if __name__ == "__main__":
    lcd = LCDScreen(LCD_SCREEN_COLUMNS, LCD_SCREEN_ROWS, LCD_RS_PIN, LCD_RW_PIN, LCD_E_PIN, LCD_DATA_PINS)
    lcd.write("Testing 1 row...")
    sleep(5)
<<<<<<< HEAD
    lcd.write("TESTING 2 rows  Second row ")
=======
    lcd.write("TESTING 2 rows.", "Second row is here")
>>>>>>> bd55b755894d4476eac5bfdb2965f3ed292b9146
    sleep(5)
    lcd.clear()
    sleep(3)
