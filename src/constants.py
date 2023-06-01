"""Constants file."""
from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
import chess

FIRST_SERVO_PIN = 18
SECOND_SERVO_PIN = 15

STEPPER_DIRECTION_PIN = 21
STEPPER_STEP_PIN = 20
STEPPER_STEP_DEGREES = 0.1125

FIRST_ARM_LENGTH_CM = 32
SECOND_ARM_LENGTH_CM = 22
ARM_HEIGHT_CM = 13

ELECTROMAGNET_PUSH_PIN = 1
ELECTROMAGNET_PULL_PIN = 7
MAGNET_PULL_DISTANCE_CM = 0.4
MAGNET_PUSH_DISTANCE_CM = 0.4

STEPPER_ZERO_POSITION_DETECT_PIN = 12
STEPPER_ZERO_POSITION_ANGLE_TO_CHESS_BOARD_CENTER_DEGREES = 45

CHESS_TILE_SIZE_CM = 5

DEFAULT_ROBOT_ARM_POSITION = (0, 30, 40)
ROBOT_ARM_DISTANCE_TO_BOARD_CM = 17.5

HORIZONTAL_DIST_TO_REMOVED_BLACKS = 25
VERTICAL_DIST_TO_REMOVED_BLACKS = 20

HORIZONTAL_DIST_TO_REMOVED_WHITES = 25
VERTICAL_DIST_TO_REMOVED_WHITES = 20

INITIAL_BOARD_STATE = [
    ["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
    ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
    ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"]
]

INITIAL_WHITE = [
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""]
]

INITIAL_BLACK = [
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""]
]


PIECE_HEIGHTS_CM = {
    "K": 10,
    "Q": 9.7,
    "B": 7.4,
    "N": 6.3,
    "R": 5.8,
    "P": 5.5
}

AngularServo.pin_factory = PiGPIOFactory()


PIECE_NAME_TYPE_DICT = {
    'P': chess.PAWN,
    'N': chess.KNIGHT,
    'B': chess.BISHOP,
    'Q': chess.QUEEN,
    'K': chess.KING
}


MAIN_BOARD_LED_PIN = 10
MAIN_BOARD_PIXEL_COUNT = 192

BLACKS_LED_PIN = 55
BLACKS_LED_COUNT = 48

WHITES_LED_PIN = 56
WHITES_LED_COUNT = 48

COLORS = {
    "white": (255, 255, 255),
    "magenta": (40, 0, 240),
    "green": (0, 255, 0),
    "light_green": (144, 238, 144),
    "light_red": (255, 114, 118)
}

ENGINE_PATH = """/usr/games/stockfish"""
ENGINE_LEVEL = 20

LCD_SCREEN_COLUMNS = 16
LCD_SCREEN_ROWS = 2
LCD_RS_PIN = 7
LCD_RW_PIN = None
LCD_E_PIN = 8
LCD_DATA_PINS = [25, 24, 23, 18]

CONTROLLER_UP_PIN = 123
CONTROLLER_DOWN_PIN = 123
CONTROLLER_LEFT_PIN = 123
CONTROLLER_RIGHT_PIN = 123
CONTROLLER_BACK_PIN = 123
CONTROLLER_ENTER_PIN = 123
