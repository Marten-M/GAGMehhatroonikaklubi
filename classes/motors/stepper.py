"""Stepper motor class file."""


class Stepper(object):
    def __init__(self, step: float):
        """
        Initialize stepper motor.

        :param step: how many degrees stepper motor turns with a single step
        """
        self.step = step

    def rotate_steps(self, steps: int):
        """
        Rotate stepper motor for given number of steps.

        If steps are negative, will rotate counter-clockwise, if positive then clockwise.

        :param steps: how many steps to take (positive or negative value)
        """
        pass