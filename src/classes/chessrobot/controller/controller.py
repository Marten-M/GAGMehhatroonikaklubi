"""Controller class file."""

from gpiozero import Button
from time import sleep


class Controller(object):
    def __init__(self, up_pin: int, down_pin: int, left_pin: int, right_pin: int, back_pin: int, enter_pin: int):
        """
        Initialize controller.

        :param up_pin: pin controlling the UP button
        :param down_pin: pin controlling the DOWN button
        :param left_pin: pin controlling the LEFT button
        :param right_pin: pin controlling the RIGHT button
        :param back_pin: pin controlling the BACK button
        :param enter_pin: pin controlling the ENTER button
        """
        self.up = Button(up_pin)
        self.down = Button(down_pin)
        self.left = Button(left_pin)
        self.right = Button(right_pin)
        self.back = Button(back_pin)
        self.enter = Button(enter_pin)

    def get_input(self) -> str:
        """
        Get user's input on the controller.

        :return: string indicating the user's input. Possible values are "UP", "DOWN", "LEFT", "RIGHT", "BACK", "ENTER"
        """
        while True:
            if self.up.is_pressed:
                return "UP"
            elif self.down.is_pressed:
                return "DOWN"
            elif self.left.is_pressed:
                return "LEFT"
            elif self.right.is_pressed:
                return "RIGHT"
            elif self.back.is_pressed:
                return "BACK"
            elif self.enter.is_pressed:
                return "ENTER"
            sleep(0.01)
