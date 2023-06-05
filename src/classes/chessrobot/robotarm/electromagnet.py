"""ElectroMagnet class file."""

from gpiozero import OutputDevice
from gpiozero.pins.native import NativeFactory
OutputDevice.pin_factory = NativeFactory()
print("aite")


class ElectroMagnet(object):
    def __init__(self, pull_pin: int, magnet_pull_distance: float):
        """
        Initialize ElectroMagnet class.

        :param pull_pin: pin controlling the electromagnet's pulling
        :param magnet_pull_distance: how far away the electromagnet can pull in cm
        """
        self.pull = OutputDevice(pull_pin)
        self.pull_distance = magnet_pull_distance
        

    def disable(self):
        """
        Disable the ElectroMagnet.
        """
        self.pull.off()
    
    def pull(self):
        """Change the electromagnet into pull mode."""
        self.pull.on()
