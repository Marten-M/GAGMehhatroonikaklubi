"""Chess board class file."""
from typing import List

chess_board = List[List[str]]

class Board(object):
    def __init__(self, initial_main_state: chess_board, initial_removed_state: List[str]):
        """
        Initialize class.

        :param initial_main_state: initial state of the board (must be 8x8 grid)
        :param initial_removed_state: initial state of the removed pieces
        """
        self.main_board = initial_main_state
        self.removed_board = initial_removed_state
        