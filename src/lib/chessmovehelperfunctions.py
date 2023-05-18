"""Helper functions in order to parse chess moves."""

from typing import Tuple


def get_coordinates_from_position(position: str) -> Tuple[int, int]:
    """
    Get integer x and y coordinates when given a chess board position.

    :param position: chess board position in short nomenclature ("e5", "d4", etc)

    :return: integer coordinates of position in the form (x, y)
    """
    return (ord(position[0].lower()) - ord('a'), int(position[1]) - 1)


def get_position_from_coordinates(x: int, y: int) -> str:
    """
    Get position from given integer coordinates.

    a1 is defined with coordinates (0, 0)

    :param x: x coordinate on chess board
    :param y: y coordinate on chess board.
    """
    return chr(ord('a') + x) + str(y + 1)
