"""ElectroMagnet class file."""

from gpiozero import OutputDevice


class ElectroMagnet(object):
    def __init__(self, pull_pin: int, push_pin: int, magnet_pull_distance: float):
        """
        Initialize ElectroMagnet class.

        :param pull_pin: pin controlling the electromagnet's pulling
        :param push_pin: pin controlling the electromagnet's pushing
        :param magnet_pull_distance: how far away the electromagnet can pull in cm
        """
        self.pull_pin = OutputDevice(pull_pin)
        self.push_pin = OutputDevice(push_pin)
        self.pull_distance = magnet_pull_distance

    def disable(self):
        """
        Disable the ElectroMagnet.
        """
        self.pull_pin.off()
        self.push_pin.off()
    
    def pull(self):
        """Change the electromagnet into pull mode."""
        self.pull_pin.on()
        self.push_pin.off()
