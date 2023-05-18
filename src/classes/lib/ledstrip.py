"""LEDStrip class file."""

from typing import Tuple
from rpi_ws281x import PixelStrip, Color


class LEDStrip(object):
    def __init__(self, led_pin: int, led_count: int, brightness: int=255, frequency: int=800_000, dma_channel: int=10, invert: bool=False, channel: int=0):
        """
        Initialize LED strip.

        :param led_pin: pin connected to the LED strip
        :param led_count: number of LED pixels
        :param brightness: brightness of the LEDs (0 - 255)
        :param frequency: signal frequency in Hz
        :param dma_channel: DMA channel to use
        :param invert: boolean indicating whether to invert the signal when using NPN transistor level shift
        :param channel: channel of the LED strip
        """
        self.strip = PixelStrip(led_count, led_pin, frequency, dma_channel, invert, brightness, channel)
        self.strip.begin()

    def set_pixel_color(self, pixel: int, color: Tuple[int, int, int]):
        """
        Set color of a pixel.

        :param pixel: pixel number of who'se color to set
        :param color: RGB color code to set pixel to in the form (red, green, blue)
        """
        self.strip.setPixelColor(pixel, Color(*color))

    def set_strip_color(self, color: Tuple[int, int, int]):
        """
        Set color of the entire LED strip.
        
        :param color: RGB color code to set the LED strip to
        """
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(*color))
