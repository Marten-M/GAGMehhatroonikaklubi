"""Game class file."""

from .board import Board
from .robotarm import RobotArm

class Game(object):
    def __init__(self, arm: RobotArm, board: Board, offset_angle: float, board_distance: float):
        """
        Initialize Game class.

        :param arm: RobotArm that moves the pieces.
        :param board: Board class describing the state of the chess board.
        :param offset_angle: how many degrees the arm is offset from the center of the board when it is in position zero.
        :param board_distance: how far away the board is from the robot arm in cm
        """
        self.arm = arm
        self.board = board
        self.arm_zero_position_offset = offset_angle
        self.arm_distance_to_board = board_distance