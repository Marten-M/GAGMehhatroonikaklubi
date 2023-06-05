"""Test for testing whether the board lighting functions work properly"""
import os
import sys

source_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, source_path)

from src.classes.chessrobot.chessboard.board import Board
from src.classes.game import Game
from src.classes.lib.ledstrip import LEDStrip
from src.constants import *

from time import sleep

if __name__ == "__main__":
    led_strip = LEDStrip(MAIN_BOARD_LED_PIN, MAIN_BOARD_PIXEL_COUNT)
    board = Board(
        INITIAL_BOARD_STATE,
        INITIAL_WHITE,
        INITIAL_BLACK,
        PIECE_HEIGHTS_CM,
        CHESS_TILE_SIZE_CM,
        led_strip,
        COLORS["white"],
        COLORS["magenta"]
    )
    green = (0, 255, 0)
    sleep(3)
    board.set_color_square("OWa4", green)
    sleep(3)
    board.set_squares_color(["a1", "b4", "e5", "OBb2"], green)
    sleep(2)

