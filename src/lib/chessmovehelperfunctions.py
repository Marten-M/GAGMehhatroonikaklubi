"""Helper functions in order to parse chess moves."""

from typing import Tuple

import chess

from ..constants import PIECE_NAME_TYPE_DICT
from ..classes.chessrobot.chessboard.piece import ChessPiece


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


def get_position_from_square_number(square: int) -> str:
    """
    Get the position from a given square number.

    :param square: square's number who'se position to get

    :return: square's position
    """
    x = chess.square_file(square)
    y = chess.square_rank(square)
    return get_position_from_coordinates(x, y)


def get_piece_type_from_name(name: str) -> chess.PieceType:
    """
    Get the chess library piece type given it's name.
    """
    name = name.upper()
    return PIECE_NAME_TYPE_DICT[name]


def get_move(starting_position: str, ending_position: str, promotion_piece: ChessPiece=None):
        """
        Get the chess library move given a starting and an ending position.

        :param starting_position: position to make the move from
        :param ending_position: position to move the piece to
        :promotion_piece: piece that will get promoted if there is a promotion
        """
        x1, y1 = get_coordinates_from_position(starting_position)
        x2, y2 = get_coordinates_from_position(ending_position)

        move = chess.Move(chess.square(x1, y1), chess.square(x2, y2))
        if promotion_piece is not None:
            move.promotion = get_piece_type_from_name(promotion_piece.name)
    
        return move