"""Constants file."""
from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory

FIRST_SERVO_PIN = 15
SECOND_SERVO_PIN = 18

STEPPER_DIRECTION_PIN = 20
STEPPER_STEP_PIN = 21
STEPPER_STEP_DEGREES = 1.8

FIRST_ARM_LENGTH_CM = 32
SECOND_ARM_LENGTH_CM = 22
ARM_HEIGHT_CM = 13

STEPPER_ZERO_POSITION_DETECT_PIN = 16

CHESS_TILE_SIZE_CM = 4


AngularServo.pin_factory = PiGPIOFactory()
