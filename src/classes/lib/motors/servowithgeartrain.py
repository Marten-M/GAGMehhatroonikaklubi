"""File for servo with a gear train and offset."""
from .servo import Servo


class GearTrainServo(Servo):
    def __init__(self, pin: int, min_pulse_ms: float=1, max_pulse_ms: float=2, pulse_frame_width_ms: float=20, gear_ratio: float=1, offset_angle: float=0, inverted: bool=False, minimum_angle: float=0, maximum_angle: float=180):
        """
        Initialize Servo motor with a gear train.

        :param pin: PWM pin controlling the servo.
        :param min_pulse_ms: pulse width in milliseconds in which the servo is at its minimal position
        :param max_pulse_ms: pulse width in milliseconds in which the servo is at its maximal position
        :param pulse_frame_width_ms: pulse frame width in milliseconds
        :param gear_ratio: ratio of the output rotation to the servo rotation
        :param offset_angle: offset angle of output gear when servo is in 0 position
        :param inverted: whether the servo angle should be inverted (0 degrees on ouput is 180 degrees on servo and vice versa)
        :param minimum_angle: minimum angle the output is able to move to
        :param maximum_angle: maximum angle the output is able to move to
        """
        super().__init__(pin, min_pulse_ms, max_pulse_ms, pulse_frame_width_ms)
        self.ratio = gear_ratio
        self.offset = offset_angle
        self.output_angle = 0
        self.inverted = inverted
        self.min_angle = minimum_angle
        self.max_angle = maximum_angle
        self.set_output_angle(self.min_angle)

    def set_output_angle(self, angle: float):
        """
        Set angle of output gear.

        :param angle: angle to set the output gear to
        """
        angle = min(max(angle, self.min_angle), self.max_angle)
        self.output_angle = angle
        actual_angle = angle * self.ratio - self.offset
        if self.inverted:
            actual_angle = 180 - actual_angle
        self.set_angle(actual_angle)

