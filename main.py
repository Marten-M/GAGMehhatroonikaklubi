from gpiozero import Button

from src.constants import *

from src.classes.lib.motors.servo import Servo
from src.classes.lib.motors.stepper import Stepper
from src.classes.lib.ledstrip import LEDStrip

from src.classes.chessrobot.robotarm.electromagnet import ElectroMagnet
from src.classes.chessrobot.robotarm.robotarm import RobotArm
from src.classes.chessrobot.controller.controller import Controller
from src.classes.lib.lcdscreen import LCDScreen
from src.classes.chessrobot.chessboard.board import Board
from src.classes.chessrobot.chessrobot import ChessRobot
from src.classes.engine import ChessEngine
from src.classes.game import Game

if __name__ == "__main__":
    first_servo = Servo(FIRST_SERVO_PIN, SERVO_MIN_POSITION_PULSE_WIDTH_MS, SERVO_MAX_POSITION_PULSE_WIDTH_MS)
    second_servo = Servo(SECOND_SERVO_PIN, SERVO_MIN_POSITION_PULSE_WIDTH_MS, SERVO_MAX_POSITION_PULSE_WIDTH_MS)
    
    stepper = Stepper(STEPPER_STEP_PIN, STEPPER_DIRECTION_PIN, STEPPER_STEP_DEGREES)
    # Zero the stepper motor
    detector = Button(STEPPER_ZERO_POSITION_DETECT_PIN)
    while not detector.is_pressed:
        stepper.rotate_steps(1)

    magnet = ElectroMagnet(ELECTROMAGNET_PULL_PIN, MAGNET_PULL_DISTANCE_CM)

    arm = RobotArm(FIRST_ARM_LENGTH_CM, SECOND_ARM_LENGTH_CM, ARM_HEIGHT_CM, stepper, first_servo, second_servo, magnet)

    main_led_strip = LEDStrip(MAIN_BOARD_LED_PIN, MAIN_BOARD_PIXEL_COUNT)

    board = Board(INITIAL_BOARD_STATE, INITIAL_WHITE, INITIAL_BLACK, PIECE_HEIGHTS_CM, CHESS_TILE_SIZE_CM, main_led_strip, COLORS["white"], COLORS["magenta"])

    controller = Controller(CONTROLLER_UP_PIN, CONTROLLER_DOWN_PIN, CONTROLLER_LEFT_PIN, CONTROLLER_RIGHT_PIN, CONTROLLER_BACK_PIN, CONTROLLER_ENTER_PIN)

    robot = ChessRobot(arm, DEFAULT_ROBOT_ARM_POSITION, board, STEPPER_ZERO_POSITION_ANGLE_TO_CHESS_BOARD_CENTER_DEGREES, ROBOT_ARM_DISTANCE_TO_BOARD_CM, HORIZONTAL_DIST_TO_REMOVED_BLACKS, VERTICAL_DIST_TO_REMOVED_BLACKS, HORIZONTAL_DIST_TO_REMOVED_WHITES, VERTICAL_DIST_TO_REMOVED_WHITES, controller, PIECE_DROPOFF_HEIGHT_CM)

    engine = ChessEngine(ENGINE_PATH, ENGINE_LEVEL)

    screen = LCDScreen(LCD_SCREEN_COLUMNS, LCD_SCREEN_ROWS, LCD_RS_PIN, LCD_RW_PIN, LCD_E_PIN, LCD_DATA_PINS)

    game = Game(robot, engine, screen,controller, COLORS["green"], COLORS["light_red"], COLORS["light_green"])
    game.run()
    
