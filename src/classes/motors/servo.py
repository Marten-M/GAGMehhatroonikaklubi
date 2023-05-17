"""Servo class file."""
from gpiozero import AngularServo
from time import sleep


class Servo(object):
    def __init__(self, pin: int):
        self.motor = AngularServo(pin)
        self.motor.angle = -90
        self.cur_angle = 0

    def set_angle(self, angle: int):
        """
        Set angle of servo motor.

        :param angle: angle to set servo to
        """
        angle = min(180, angle) if angle > 0 else 0
        if self.cur_angle < angle:
            for i in range(self.cur_angle, angle + 1):
                self.motor.angle = i - 90
                sleep(0.03)
        else:
            for i in range(self.cur_angle, angle - 1, -1):
                self.motor.angle = i - 90
                sleep(0.03)
