from gpiozero import Button

from constants import *

from src.classes.motors.servo import Servo
from src.classes.motors.stepper import Stepper

from src.classes.robotarm import RobotArm


if __name__ == "__main__":
    first_servo = Servo(FIRST_SERVO_PIN)
    second_servo = Servo(SECOND_SERVO_PIN)
    
    stepper = Stepper(STEPPER_STEP_PIN, STEPPER_DIRECTION_PIN, STEPPER_STEP_DEGREES)
    # Zero the stepper motor
    detector = Button(STEPPER_ZERO_POSITION_DETECT_PIN)
    while not detector.is_pressed:
        stepper.rotate_steps(1)

    arm = RobotArm(FIRST_ARM_LENGTH_CM, SECOND_ARM_LENGTH_CM, ARM_HEIGHT_CM, stepper, first_servo, second_servo)

    import time
    while True:
        arm.move_arm_to_position(12, 20, 10)
        time.sleep(2)
        arm.move_arm_to_position(20, 40, 5)
