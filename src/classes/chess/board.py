"""Chess board class file."""
from typing import List

chess_board = List[List[str]]

class Board(object):
    def __init__(self, initial_main_state: chess_board, initial_removed_state: List[str], piece_heights: dict, chess_tile_size: float):
        """
        Initialize class.

        :param initial_main_state: initial state of the board (must be 8x8 grid)
        :param initial_removed_state: initial state of the removed pieces
        :param piece_heights: heights of the pieces.
        :param chess_tile_size: size of a chess tile's side in cm
        """
        self.main_board = initial_main_state
        self.removed_board = initial_removed_state
        self.heights = piece_heights
        self.chess_tile_side_length = chess_tile_size
        
    def get_height(self, piece: str):
        """
        Get the height of a given piece.

        :param piece: short chess notation of piece who'se height to get
        """
        return self.heights[piece]
    
    def __getitem__(self, key: int) -> List[str]:
        """
        Get a chess board row.
        """
        return self.main_board[key]
