from constants import FIRST_SERVO_PIN, SECOND_SERVO_PIN, STEPPER_STEP_DEGREES, FIRST_ARM_LENGTH_CM, SECOND_ARM_LENGTH_CM, \
                      ARM_HEIGHT_CM

from classes.motors.servo import Servo
from classes.motors.stepper import Stepper

from classes.robotarm import RobotArm

if __name__ == "__main__":
    first_servo = Servo(FIRST_SERVO_PIN)
    second_servo = Servo(SECOND_SERVO_PIN)
    stepper = Stepper(STEPPER_STEP_DEGREES)

    arm = RobotArm(FIRST_ARM_LENGTH_CM, SECOND_ARM_LENGTH_CM, ARM_HEIGHT_CM, stepper, first_servo, second_servo)
    
    import time
    while True:
        arm.move_arm_to_position(12, 20, 10)
        time.sleep(2)
        arm.move_arm_to_position(12, 40, 5)
