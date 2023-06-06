"""Game class file."""

from typing import Tuple

from .chessboard.board import Board
from .controller.controller import Controller
from .chessboard.piece import ChessPiece

from .robotarm.robotarm import RobotArm

from ...lib.chessmovehelperfunctions import get_coordinates_from_position
from ...lib.mathfunctions import calc_vector_length, arctan


class ChessRobot(object):
    def __init__(self, arm: RobotArm, default_arm_position: tuple, board: Board, offset_angle: float, board_distance: float, horizontal_dist_to_black_removed: float, vertical_dist_to_black_removed: float, horizontal_dist_to_white_removed: float, vertical_dist_to_white_removed: float, controller: Controller, piece_dropoff_height: float):
        """
        Initialize Game class.

        :param arm: RobotArm that moves the pieces.
        :param default_arm_position: the default position of the arm.
        :param board: Board class describing the state of the chess board.
        :param offset_angle: how many degrees the arm is offset from the center of the board when it is in position zero.
        :param board_distance: how far away the board is from the robot arm in cm
        :param horizontal_dist_to_black_removed: horizontal distance to removed black pieces section's edge in cm
        :param vertical_dist_to_black_removed: vertical distance to removed black pieces section's edge in cm
        :param horizontal_dist_to_white_removed: horizontal distance to removed white pieces section's edge in cm
        :param vertical_dist_to_white_removed: vertical distance to removed white pieces section's edge in cm
        :param controller: Controller object for selecting and making moves
        :param piece_dropoff_height: how far away from the floor the piece should be dropped off when it is held in cm
        """
        self.arm = arm
        self.board = board
    
        self.arm_zero_position_offset = offset_angle
        self.arm_distance_to_board = board_distance

        self.horizontal_distance_to_black_removed = horizontal_dist_to_black_removed
        self.vertical_distance_to_black_removed = vertical_dist_to_black_removed

        self.horizontal_distance_to_white_removed = horizontal_dist_to_white_removed
        self.vertical_distance_to_white_removed = vertical_dist_to_white_removed

        self.default_arm_position = default_arm_position
        self.controller = controller

        self.piece_dropoff_height_offset = piece_dropoff_height

    def get_robot_arm_parameters(self, target_position: str, target_height: float) -> Tuple[float, float, float]:
        """
        Get parameters to pass into robot arm in order to move the arm to correct position.

        :param target_position: target chess position in short nomenclature ("e4", "d6", etc)
        :param target_height: target height the robot arm should go to in cm

        :return: tuple of floats indicating the `RobotArm.move_arm_to_position` function parameters
        """
        if target_position[0] != "O":
            x, y = get_coordinates_from_position(target_position)

            vertical_distance = self.arm_distance_to_board + self.board.chess_tile_side_length * (0.5 + (7 - y))
            print(f"Vertical distance: {vertical_distance}")
            
            x_from_center = 3 - x if x <= 3 else 3 - (7 - x)
            horizontal_distance = self.board.chess_tile_side_length * (0.5 + x_from_center)
            print(f"Horizontal distance: {horizontal_distance}")

            total_dist = calc_vector_length(horizontal_distance, vertical_distance)

            angle = 90 - arctan(horizontal_distance / vertical_distance) + self.arm_zero_position_offset
            
            if x >= 4:
                angle += 90
            print(f"angle: {angle}")

        else:
            color = 1 if target_position[1] == "W" else 0
            target_position = target_position[2:]
            x, y = get_coordinates_from_position(target_position)
            if color:
                vertical_distance = self.vertical_distance_to_white_removed + self.board.chess_tile_side_length * (0.5 + (7 - y))
                horizontal_distance = self.horizontal_distance_to_white_removed + self.board.chess_tile_side_length * (0.5 + (1 - x))
                angle = 90 - arctan(horizontal_distance / vertical_distance) + self.arm_zero_position_offset
            else:
                vertical_distance = self.vertical_distance_to_black_removed + self.board.chess_tile_side_length * (0.5 + (7 - y))
                horizontal_distance = self.horizontal_distance_to_black_removed + self.board.chess_tile_side_length * (0.5 + x)
                angle = 90 - arctan(horizontal_distance / vertical_distance) + 90 + self.arm_zero_position_offset
            
            total_dist = calc_vector_length(horizontal_distance, vertical_distance)

        return (angle, total_dist, target_height)

    def move_piece(self, starting_position: str, ending_position: str):
        """
        Move a piece from one position to another.

        It is expected that the ending position is not occupied and the starting position is and that the robot arm is lifted up in the beginning.

        :param starting_position: starting position of piece to move.
        :param ending_position: ending position of piece to move.
        """
        piece = self.board.get_piece(starting_position)
        # pick up the piece
        self.pick_up_piece(piece)
        self.board.set_position_value(None, starting_position)
        # place the piece
        self.place_piece(piece, ending_position)
        self.board.set_position_value(piece, ending_position)
        piece.position = ending_position

    def pick_up_piece(self, piece: ChessPiece):
        """
        Pick up a piece and move robot arm to default position.

        :param piece: Chess piece to pick up
        """
        params = self.get_robot_arm_parameters(piece.position, piece.height + self.arm.electromagnet.pull_distance)
        self.arm.move_arm_to_position(*params)
        self.arm.electromagnet.pull()
        self.arm.move_arm_to_position(params[0], params[1], params[2] + 13)
        self.arm.move_arm_to_position(*self.default_arm_position)

    def place_piece(self, piece: ChessPiece, target_position: str):
        """
        Place a piece on the board and move the arm to default position.

        :param piece: piece to place that robot is currently holding
        :param target_position: target position to move the piece to
        """
        params = self.get_robot_arm_parameters(target_position, piece.height + self.piece_dropoff_height_offset)
        self.arm.move_arm_to_position(*params)
        self.arm.move_arm_to_position(params[0], params[1], params[2] + 13)
        self.arm.electromagnet.disable()
        self.arm.move_arm_to_position(*self.default_arm_position)

    def castle(self, starting_position: str, ending_position: str) -> bool:
        """
        Castle the king if that was the move that was made.

        It is assumed castling is possible and the starting and ending position are those of the king.

        :param starting_position: starting position of the king
        :param ending_position: ending position of the king
        
        :return: whether the castling was done
        """
        if starting_position == "e1": # White castled
            if ending_position == "g1": # Short castle
                rook = self.board.get_piece("h1")
                self.move_piece(starting_position, ending_position)
                self.move_piece(rook.position, "f1")
                return True
            elif ending_position == "c1": # Long castle
                rook = self.board.get_piece("a1")
                self.move_piece(starting_position, ending_position)
                self.move_piece(rook.position, "d1")
                return True
        elif starting_position == "e8": # Black castled
            if ending_position == "g8":
                rook = self.board.get_piece("h8")
                self.move_piece(starting_position, ending_position)
                self.move_piece(rook.position, "f8")
                return True
            elif ending_position == "c8": # Long castle
                rook = self.board.get_piece("a8")
                self.move_piece(starting_position, ending_position)
                self.move_piece(rook.position, "d8")
                return True

        return False

    def make_chess_move(self, starting_position: str, ending_position: str, promotion_piece: ChessPiece=None):
        """
        Make a legal chess move from one position to another.

        :param starting_position: starting position of the piece to move
        :param ending_position: ending position of the piece to move
        :param promotion_piece: piece that was selected for promotion (if there was a promotion)
        """
        ending_piece = self.board.get_piece(ending_position)
        if ending_piece is not None:
            removed_piece_destination = self.board.get_first_free_position(ending_piece.color)
            self.move_piece(ending_piece.position, removed_piece_destination)

        starting_piece = self.board.get_piece(starting_position)
        print(f"starting piece: {starting_piece.position}")
        # Check if it is a pawn making a promotion
        if promotion_piece is not None:
            destination = self.board.get_first_free_position(starting_piece.color)
            self.move_piece(starting_piece.position, destination)
            self.move_piece(promotion_piece.position, ending_position)
        elif starting_piece.name.upper() == 'K':
            if not self.castle(starting_position, ending_position):
                self.move_piece(starting_position, ending_position)
        else:
            self.move_piece(starting_position, ending_position)
