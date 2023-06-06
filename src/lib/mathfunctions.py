"""Functions file."""
import numpy as np
import math


def arcsin(value: float) -> float:
    """
    Get arcsin of value in degrees.

    :param value: value to take arcsin of

    :return: angle in degrees
    """
    return float(round(np.arcsin(value) * 180 / math.pi, 3))


def arccos(value: float) -> float:
    """
    Get arccos of value in degrees.

    :param value: value to take arccos of

    :return: angle in degrees
    """
    return float(round(np.arccos(value) * 180 / math.pi, 3))


def arctan(value: float) -> float:
    """
    Get arctan of value in degrees.

    :param value: value to take arctan of

    :return: angle in degrees.
    """
    return float(round(np.arctan(value) * 180 / math.pi, 3))


def get_area_heron(side1: float, side2: float, side3: float) -> float:
    """
    Calculate area of triangle using heron's formula.

    :param side1: length of side 1 in cm
    :param side2: length of side 2 in cm
    :param side3: length of side 3 in cm

    :return: area of triangle in cm^2
    """
    p = (side1 + side2 + side3) / 2
    area = (p * (p - side1) * (p - side2) * (p - side3)) ** 0.5
    return area


def get_angle_between_triangle_sides(area: float, side1: float, side2: float) -> float:
    """
    Calculate angle between 2 sides in a triangle.

    :param area: area of triangle in cm^2
    :param side1: length of first side in cm
    :param side2: length of second side in cm

    :return: angle between given sides in degrees
    """
    sin_angle = 2 * area / (side1 * side2)
    return arcsin(sin_angle)


def calc_vector_length(x: float, y: float) -> float:
    """
    Calculate a vector's length.

    :param x: x coordinate of vector
    :param y: y coordinate of vector
    """
    return (x ** 2 + y ** 2) ** 0.5
