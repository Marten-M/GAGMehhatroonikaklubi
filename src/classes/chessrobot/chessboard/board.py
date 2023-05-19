"""Chess board class file."""
from typing import List, Tuple, Dict

from .piece import ChessPiece

from ...lib.ledstrip import LEDStrip

from ....lib.chessmovehelperfunctions import get_position_from_coordinates, get_coordinates_from_position

chess_board = List[List[str]]

class Board(object):
    def __init__(self, initial_main_state: chess_board, initial_removed_whites_state: chess_board, initial_removed_blacks_state: chess_board, piece_heights: dict, chess_tile_size: float, main_led_strip: LEDStrip, whites_led_strip: LEDStrip, blacks_led_strip: LEDStrip, white: Tuple[int, int, int], black: Tuple[int, int, int]):
        """
        Initialize class.

        :param initial_main_state: initial state of the board (must be 8x8 grid)
        :param initial_removed__whites_state: initial state of the removed white pieces (must be 2x8 grid)
        :param initial_removed_blacks_state: initial state of the removed black pieces (must be 2x8 grid)
        :param piece_heights: heights of the pieces.
        :param chess_tile_size: size of a chess tile's side in cm
        :param main_led_strip: LEDStrip that lights up the squares beneath the main chess board
        :param whites_led_strip: LEDStrip that lights up the squares beneath the removed white pieces
        :param blacks_led_strip: LEDStrip that lights up the squares beneath the removed black pieces
        :param white: RGB color code of the white squares
        :param black: RGB color code of the black squares
        """
        self.heights = piece_heights
        self.chess_tile_side_length = chess_tile_size
        # Initialize boards
        self.main_board = self.initialize_main_board(initial_main_state)
        self.removed_whites = self.initialize_removed_board(initial_removed_whites_state)
        self.removed_blacks = self.initialize_removed_board(initial_removed_blacks_state)

        self.main_board_led_strip = main_led_strip
        self.removed_whites_led_strip = whites_led_strip
        self.removed_blacks_led_strip = blacks_led_strip

        self.black_square_color = black
        self.white_square_color = white

        self.color_boards()

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

    def get_square_leds(self, square: str) -> Tuple[int, int, int]:
        """
        Get the leds under a specific square.

        :param square: square short chess nomenclature (a1, d4, OBa2 etc)
        """
        if square[0].upper() == 'O':
            x, y = get_coordinates_from_position(square[2:])
        else:
            x, y = get_coordinates_from_position(square)
        
        if x % 2 == 0:
            start_led = 7 - y + x * 8
        else:
            start_led = x * 8 + y
        
        start_led *= 3
        return (start_led, start_led + 1, start_led + 2)

    def set_color_square(self, square: str, color: Tuple[int, int, int]):
        """
        Set color of a square.

        :param square: square who'se color to set in short chess nomenclature (a1, d4, OBa2, etc)
        :param color: RGB color code to set the squares color to
        """
        squares = self.get_square_leds(square)
        if square[0].upper() == 'O':
            if square[1].upper() == 'W':
                for pixel in squares:
                    self.removed_blacks_led_strip.set_pixel_color(pixel, color)
            else:
                for pixel in squares:
                    self.removed_whites_led_strip.set_pixel_color(pixel, color)
        else:
            for pixel in squares:
                self.main_board_led_strip.set_pixel_color(pixel, color)

    def set_squares_color(self, squares: List[str], color: Tuple[int, int, int]):
        """
        Set color of multiple squares.

        :param squares: list of squares in short chess nomenclature (a1, d4, OBa2, etc)
        :param color: RGB color code to set the squares to
        """
        for square in squares:
            self.set_color_square(square, color)

    def color_boards(self):
        """Color the chess board squares."""
        self.removed_blacks_led_strip.set_strip_color(self.white_square_color)
        self.removed_whites_led_strip.set_strip_color(self.white_square_color)

        for y in range(8):
            for x in range(8):
                square = get_position_from_coordinates(x, y)
                if y % 2 == 0:
                    if x % 2 == 0:
                        self.set_color_square(square, self.black_square_color)
                    else:
                        self.set_color_square(square, self.white_square_color)
                else:
                    if x % 2 == 0:
                        self.set_color_square(square, self.white_square_color)
                    else:
                        self.set_color_square(square, self.black_square_color)

    def get_possible_pieces_for_promotion(self, color: int) -> Dict[str, ChessPiece]:
        """
        Get possible pieces to promote to for given color.

        :param color: color of player who is promoting their pawn

        :return: dictionary mapping piece names to their ChessPiece counterparts
        """
        dic = dict()
        removed_board = self.removed_whites if color else self.removed_blacks
        for y in range(2):
            for x in range(8):
                piece = removed_board[y][x]
                if piece.name.upper() in "QRBN":
                    dic[piece.name.upper()] = piece
        
        return dic

    def __getitem__(self, key: int) -> List[str]:
        """
        Get a chess board row.
        """
        return self.main_board[key]

