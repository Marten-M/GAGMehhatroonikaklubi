"""Stepper motor class file."""
from gpiozero import OutputDevice
from time import sleep


class Stepper(object):
    def __init__(self, step_pin: int, direction_pin: int, step: float):
        """
        Initialize stepper motor.
        
        :param step_pin: pin that sends out step control signals
        :param direction_pin: pin that controls direction of stepper motor
        :param step: how many degrees stepper motor turns with a single step
        """
        self.step_sender = OutputDevice(step_pin, active_high=True)
        self.direction = OutputDevice(direction_pin)
        self.step = step

    def rotate_steps(self, steps: int):
        """
        Rotate stepper motor for given number of steps.

        If steps are negative, will rotate counter-clockwise, if positive then clockwise.

        :param steps: how many steps to take (positive or negative value)
        """
        if steps >= 0:
            self.direction.off()
        else:
            self.direction.on()

        for i in range(abs(steps)):
            self.step_sender.off()
            sleep(0.001)
            self.step_sender.on()
