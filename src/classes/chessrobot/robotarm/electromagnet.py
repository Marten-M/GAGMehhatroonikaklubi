"""ElectroMagnet class file."""

from gpiozero import OutputDevice


class ElectroMagnet(object):
    def __init__(self, pull_pin: int, push_pin: int, magnet_pull_distance: float, magnet_push_distance: float):
        """
        Initialize ElectroMagnet class.

        :param pull_pin: pin controlling the electromagnet's pulling
        :param push_pin: pin controlling the electromagnet's pushing
        :param magnet_pull_distance: how far away the electromagnet can pull in cm
        :param magnet_push_distance: how far away the electromagnet can push in cm
        """
        self.pull = OutputDevice(pull_pin)
        self.push = OutputDevice(push_pin)
        self.pull_distance = magnet_pull_distance
        self.push_distance = magnet_push_distance

    def disable(self):
        """
        Disable the ElectroMagnet.
        """
        self.pull.on()
        self.push.on()
    
    def pull(self):
        """Change the electromagnet into pull mode."""
        self.pull.on()
        self.push.off()
    
    def push(self):
        """Change the electromagnet into push mode."""
        self.pull.off()
        self.push.on()
