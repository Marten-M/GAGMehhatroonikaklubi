"""LCDScreen class file."""

from typing import List

from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO


class LCDScreen(object):
    def __init__(self, columns: int, rows: int, rs_pin: int, rw_pin: int, e_pin: int, data_pins: List[int], numbering_mode=GPIO.BCM):
        """
        Initialize the LCD screen.

        :param columns: number of columns on the LCD screen
        :param rows: number of rows on the LCD screen
        :param rs_pin: RS (data/instruction select) pin
        :param rw_pin: R/W (read/write select) pin
        :param e_pin: Enable pin
        :param data_pins: list of data pin numbers
        """
        self.lcd = CharLCD(cols=columns, rows=rows, pin_rs=rs_pin, pin_rw=rw_pin, pin_e=e_pin, pins_data=data_pins, numbering_mode=numbering_mode)
        self.clear()

    def write(self, text: str):
        """
        Write text to the LCD display.

        Lines that are too long automatically continue on next line

        :param text: text to write. Use '\n' to write to new line.
        """
        self.lcd.write_string(text)
    
    def clear(self):
        """
        Clear the screen.
        """
        self.lcd.clear()