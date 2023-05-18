"""Game class file."""

from typing import Tuple

from .board import Board
from ..robotarm.robotarm import RobotArm

from ...lib.chessmovehelperfunctions import get_coordinates_from_move
from ...lib.mathfunctions import calc_vector_length, arctan

class Game(object):
    def __init__(self, arm: RobotArm, board: Board, offset_angle: float, board_distance: float, magnet_pull_height: float):
        """
        Initialize Game class.

        :param arm: RobotArm that moves the pieces.
        :param board: Board class describing the state of the chess board.
        :param offset_angle: how many degrees the arm is offset from the center of the board when it is in position zero.
        :param board_distance: how far away the board is from the robot arm in cm
        :param magnet_pull_height: how far away (in cm) the magnet should be from the top of the button in order to pull it
        """
        self.arm = arm
        self.board = board
        self.arm_zero_position_offset = offset_angle
        self.arm_distance_to_board = board_distance

    def get_robot_arm_parameters(self, target_position: str, target_height: float) -> Tuple[float, float, float]:
        """
        Get parameters to pass into robot arm in order to move the arm to correct position.

        :param target_position: target chess position in short nomenclature ("e4", "d6", etc)
        :param target_height: target height the robot arm should go to in cm

        :return: tuple of floats indicating the `RobotArm.move_arm_to_position` function parameters
        """
        x, y = get_coordinates_from_move(target_position)

        vertical_distance = self.arm_distance_to_board + self.board.chess_tile_side_length * (0.5 + (7 - y))
        
        x_from_center = 3 - x if x <= 3 else 3 - (7 - x)
        horizontal_distance = self.board.chess_tile_side_length * (0.5 + x_from_center)

        total_dist = calc_vector_length(horizontal_distance, vertical_distance)

        angle = arctan(horizontal_distance / vertical_distance)
        if x >= 4:
            angle *= 2

        angle += self.arm_zero_position_offset

        return (angle, total_dist, target_height)

    def remove_piece_from_board()       

