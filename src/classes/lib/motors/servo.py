"""Servo class file."""
from gpiozero import AngularServo
from time import sleep


class Servo(object):
    def __init__(self, pin: int, min_pulse_ms: float=1, max_pulse_ms: float=2, pulse_frame_width_ms: float=20, inverted: bool=False):
        """
        Initialize Servo motor.

        :param pin: PWM pin controlling the servo.
        :param min_pulse_ms: pulse width in milliseconds in which the servo is at its minimal position
        :param max_pulse_ms: pulse width in milliseconds in which the servo is at its maximal position
        :param pulse_frame_width_ms: pulse frame width in milliseconds
        """
        self.motor = AngularServo(pin, min_pulse_width=min_pulse_ms / 1000, max_pulse_width=max_pulse_ms / 1000, frame_width=pulse_frame_width_ms / 1000)
        angle = self.motor.angle
        self.inverted = inverted
        if angle is not None:
            self.cur_angle = int(90 + self.motor.angle)
            self.set_angle(90)
        else:
            self.motor.angle = 0
            self.cur_angle = 90

    def set_angle(self, angle: float):
        """
        Set angle of servo motor.

        :param angle: angle to set servo to
        """

        angle = min(180, angle) if angle > 0 else 0
        if self.cur_angle <= angle:
            for i in range(self.cur_angle, int(angle) + 1):
                self.motor.angle = i - 90
                sleep(0.05)
        else:
            for i in range(self.cur_angle, int(angle) - 1, -1):
                self.motor.angle = i - 90
                sleep(0.05)
        self.motor.angle = angle - 90
        self.cur_angle = angle

