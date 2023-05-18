"""Chess board class file."""
from typing import List

from .piece import ChessPiece
from ..controller.controller import Controller

from ....lib.chessmovehelperfunctions import get_position_from_coordinates, get_coordinates_from_position

chess_board = List[List[str]]

class Board(object):
    def __init__(self, initial_main_state: chess_board, initial_removed_whites_state: chess_board, initial_removed_blacks_state: chess_board, piece_heights: dict, chess_tile_size: float):
        """
        Initialize class.

        :param initial_main_state: initial state of the board (must be 8x8 grid)
        :param initial_removed__whites_state: initial state of the removed white pieces (must be 2x8 grid)
        :param initial_removed_blacks_state: initial state of the removed black pieces (must be 2x8 grid)
        :param piece_heights: heights of the pieces.
        :param chess_tile_size: size of a chess tile's side in cm
        """
        self.heights = piece_heights
        self.chess_tile_side_length = chess_tile_size
        # Initialize boards
        self.main_board = self.initialize_main_board(initial_main_state)
        self.removed_whites = self.initialize_removed_board(initial_removed_whites_state)
        self.removed_blacks = self.initialize_removed_board(initial_removed_blacks_state)

    def initialize_main_board(self, board: chess_board):
        """
        Initialize the main board from strings into chess pieces.

        :param board: board to initialize

        :return: initialized board
        """
        for y in range(8):
            for x in range(8):
                piece = board[y][x]
                if piece:
                    color = 1 if piece[0].upper() == 'W' else 0
                    name = piece[1].upper()
                    position = get_position_from_coordinates(x, y)
                    board[y][x] = ChessPiece(name, position, self.heights[name], color)
                else:
                    board[y][x] = None

        return board
    
    def initialize_removed_board(self, board: chess_board, color: int):
        """
        Initialize removed board.

        :param board: board to initialize
        :param color: color to give to pieces
        
        :return: initialized board
        """
        for y in range(2):
            for x in range(8):
                piece = board[y][x]
                if piece:
                    name = piece[1].upper()
                    position = f"O{'W' if color else 'B'}" + get_position_from_coordinates(x, y)
                    board[y][x] = ChessPiece(name, position, self.heights[name], color)
                else:
                    board[y][x] = None
        
        return board
    
    def get_piece(self, position: str) -> ChessPiece:
        """
        Get the chess piece at a given location.

        :param position: position of the chess piece to get.
        """
        if position[0].upper() == "O":
            x, y = get_coordinates_from_position(position[2:])
            if position[1].upper() == "W":
                return self.removed_whites[y][x]
            else:
                return self.removed_blacks[y][x]
        
        x, y = get_coordinates_from_position(position)

        return self.main_board[y][x]
    
    def get_first_free_position(self, color: int) -> str:
        """
        Get first free position to move a removed piece to.

        :param color: color of the piece that is about to be removed from the main board
        """
        board = self.removed_whites if color else self.removed_blacks
        for y in range(2):
            for x in range(8):
                if board[y][x] is None:
                    return f"O{'W' if color else 'B'}{get_position_from_coordinates(y, x)}"

    def set_position_value(self, value, position: str):
        """
        Set the value of a given board position.

        :param value: value to set to. Could be either None or a ChessPiece
        :param position: chess board position who'se value to set
        """
        if position[0].upper() == 'O':
            x, y = get_coordinates_from_position(position[2:])
            if position[1].upper() == 'W':
                self.removed_whites[y][x] = value
            else:
                self.removed_blacks[y][x] = value
        else:
            x, y = get_coordinates_from_position(position)
            self.main_board[y][x] = value

    def __getitem__(self, key: int) -> List[str]:
        """
        Get a chess board row.
        """
        return self.main_board[key]

