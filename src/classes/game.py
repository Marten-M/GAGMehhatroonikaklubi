"""Game class file."""

import keyboard

import chess
from time import sleep
from typing import Tuple

from .engine import ChessEngine

from .lib.lcdscreen import LCDScreen

from .chessrobot.chessrobot import ChessRobot
from .chessrobot.chessboard.piece import ChessPiece
from .chessrobot.controller.controller import Controller

from ..lib.chessmovehelperfunctions import get_coordinates_from_position, get_position_from_coordinates, get_position_from_square_number, get_move, get_piece_type_from_name

color = Tuple[int, int, int]

class Game(object):
    def __init__(self, robot: ChessRobot, engine: ChessEngine, screen: LCDScreen, controller: Controller, selection_color: color, last_move_color: color, possible_moves_color: color):
        """
        Initialize chess game.

        :param robot: ChessRobot that moves the pieces and controls the board
        :param engine: ChessEngine to play against player
        :param selection_color: color of current selection square
        :param last_move_color: color of last move that opponent made
        :param possible_moves_color: color of possible moves you can make
        """
        self.robot = robot
        self.game = chess.Board()
        self.engine = engine
        self.screen = screen
        self.controller = controller

        self.cur_selection = "d2"
        self.last_selection = "d2"
        self.last_move = []
        self.possible_moves = []
        self.possible_selections = []

        self.selection_color = selection_color
        self.last_move_color = last_move_color
        self.possible_moves_color = possible_moves_color
        
        self.selected = False # Tracking whether a square has been selected or not
        self.player_color = 1

        self.selecting_promotion = False
        self.color_squares()



    def run(self):
        """
        Run the chess game.
        """
        while True:
            # action = self.controller.get_input()
            action = self.controller.get_input()
            x, y = get_coordinates_from_position(self.cur_selection)
            """
            ———————————No switches?———————————
            ⠀⣞⢽⢪⢣⢣⢣⢫⡺⡵⣝⡮⣗⢷⢽⢽⢽⣮⡷⡽⣜⣜⢮⢺⣜⢷⢽⢝⡽⣝
            ⠸⡸⠜⠕⠕⠁⢁⢇⢏⢽⢺⣪⡳⡝⣎⣏⢯⢞⡿⣟⣷⣳⢯⡷⣽⢽⢯⣳⣫⠇
            ⠀⠀⢀⢀⢄⢬⢪⡪⡎⣆⡈⠚⠜⠕⠇⠗⠝⢕⢯⢫⣞⣯⣿⣻⡽⣏⢗⣗⠏⠀
            ⠀⠪⡪⡪⣪⢪⢺⢸⢢⢓⢆⢤⢀⠀⠀⠀⠀⠈⢊⢞⡾⣿⡯⣏⢮⠷⠁⠀⠀
            ⠀⠀⠀⠈⠊⠆⡃⠕⢕⢇⢇⢇⢇⢇⢏⢎⢎⢆⢄⠀⢑⣽⣿⢝⠲⠉⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⡿⠂⠠⠀⡇⢇⠕⢈⣀⠀⠁⠡⠣⡣⡫⣂⣿⠯⢪⠰⠂⠀⠀⠀⠀
            ⠀⠀⠀⠀⡦⡙⡂⢀⢤⢣⠣⡈⣾⡃⠠⠄⠀⡄⢱⣌⣶⢏⢊⠂⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⢝⡲⣜⡮⡏⢎⢌⢂⠙⠢⠐⢀⢘⢵⣽⣿⡿⠁⠁⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠨⣺⡺⡕⡕⡱⡑⡆⡕⡅⡕⡜⡼⢽⡻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⣼⣳⣫⣾⣵⣗⡵⡱⡡⢣⢑⢕⢜⢕⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⣴⣿⣾⣿⣿⣿⡿⡽⡑⢌⠪⡢⡣⣣⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⡟⡾⣿⢿⢿⢵⣽⣾⣼⣘⢸⢸⣞⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠁⠇⠡⠩⡫⢿⣝⡻⡮⣒⢽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            —————————————————————————————-----
            """
            if not self.selected:
                self.screen.write("Vali nupp mida liigutada")
            else:
                self.screen.write("Vali ruut kuhu nupp käia")
            if action == "UP":
                y = min(7, y + 1)
            elif action == "DOWN":
                y = max(0, y - 1)
            elif action == "LEFT":
                x = max(0, x - 1)
            elif action == "RIGHT":
                x = min(7, x + 1)
            elif action == "BACK" and self.selected:
                self.selected = False
            elif action == "ENTER":
                if not self.selected:
                    if self.selection_legal(self.player_color):
                        self.selected = True
                        self.last_selection = self.cur_selection
                else:
                    if self.cur_selection in self.possible_moves:
                        self.make_move(self.last_selection, self.cur_selection)
                        self.screen.write("Vastane käib...")
                        self.make_engine_move()
            self.cur_selection = get_position_from_coordinates(x, y)
            if not self.selected:
                self.update_possible_moves()
            self.color_squares()
            if self.game.is_game_over():
                winner = self.game.outcome().winner
                if winner is None:
                    self.screen.write("Viik!")
                elif winner: # White won
                    self.screen.write("Valge võitis!")
                else:
                    self.screen.write("Must võitis!")
                return

    def selection_legal(self, color: int) -> bool:
        """
        Detect whether current selection is legal or not.

        :param color: color of player that is selecting a piece

        :return: boolean indicating if selecting a piece is legal
        """
        return self.robot.board.get_piece(self.cur_selection).color == color

    def make_move(self, starting_position: str, ending_position: str, promotion_piece: ChessPiece = None) -> bool:
        """
        Make a given move on the board.

        Prompts for promotion piece selection, if it is a promotion.

        :param starting_position: position to make the move from
        :param ending_position: position to move the piece to
        :param promotion_piece: piece to promote to if promotion is happening
        """
        piece = self.robot.board.get_piece(starting_position)
        x, y = get_coordinates_from_position(ending_position)
        chess_move = get_move(starting_position, ending_position, promotion_piece)
        if piece.name.upper() == 'P' and y == 7: # Player is promoting
            promotion_piece = self.robot.board.get_piece(self.get_promotion_piece_selection(self.player_color))
        self.screen.write("Sina käid...")
        self.robot.make_chess_move(starting_position, ending_position, promotion_piece)
        self.game.push(chess_move)

    def get_promotion_piece_selection(self, color: int) -> str:
        """
        Get the promotion piece selection for a given player.

        :param color: color of player who chooses a promotable piece
        
        :return: position of piece that was chosen
        """
        self.cur_selection = "OWa1"
        self.screen.write("Vali nupp, milleks ettur muuta")
        self.selecting_promotion = True
        pieces = self.robot.board.get_possible_pieces_for_promotion(color)
        self.possible_selections = []
        for key in pieces:
            for piece in pieces[key]:
                self.possible_selections.append(piece.position)
        while True:
            action = self.get_input()
            x, y = get_coordinates_from_position(self.cur_selection[2:])
            if action == "UP":
                y = min(7, y + 1)
            elif action == "DOWN":
                y = max(0, y - 1)
            elif action == "LEFT":
                x = 0
            elif action == "RIGHT":
                x = 1
            elif action == "ENTER":
                if self.cur_selection in self.possible_selections:
                    return self.cur_selection

            self.cur_selection = 'OW' + get_position_from_coordinates(x, y)
            self.color_squares()

    def make_engine_move(self):
        """
        Make engine move.
        """
        move = self.engine.engine.play(self.game, chess.engine.Limit(time=0.1))
        piece = None
        if move.promotion is not None:
            possible_pieces = self.robot.board.get_possible_pieces_for_promotion(0)
            if possible_pieces.get('Q', None) is not None:
                piece = possible_pieces['Q'][0]
            elif possible_pieces.get('R', None) is not None:
                piece = possible_pieces['R'][0]
            elif possible_pieces.get('B', None) is not None:
                piece = possible_pieces['B'][0]
            elif possible_pieces.get('N', None) is not None:
                piece = possible_pieces['N'][0]
            move.promotion = get_piece_type_from_name(piece.name)

        from_square = get_position_from_square_number(move.from_square)
        to_square = get_position_from_square_number(move.to_square)
        self.make_move(from_square, to_square, piece)
        self.game.push(move)
        self.last_move = [from_square, to_square]

    def get_input(self) -> str:
        """
        Get input from player.

        Currently uses keyboard. Should be changed later.

        :return: event that should happen
        """
        key = keyboard.read_key()

        dic = {
            'w': "UP",
            's': "DOWN",
            'a': "RIGHT",
            'd': "LEFT",
            'r': "BACK",
            'p': "ENTER"
        }
        return dic[key]

    def update_possible_moves(self):
        """
        Update possible moves based on current location.
        """
        square = chess.square(*get_coordinates_from_position(self.cur_selection))
        self.possible_moves = []
        for move in self.game.legal_moves:
            if move.from_square == square:
                self.possible_moves.append(get_position_from_square_number(move.to_square))

    def color_squares(self):
        """
        Color squares the necessary color.
        """
        self.robot.board.color_boards()
        self.robot.board.set_squares_color(self.last_move, self.last_move_color)
        self.robot.board.set_squares_color(self.possible_moves, self.possible_moves_color)

        for piece in self.possible_selections:
            self.robot.board.set_color_square(piece.position, self.possible_moves_color)

        if not self.selecting_promotion and self.selected:
            self.robot.board.set_color_square(self.last_selection, self.possible_moves_color)
        self.robot.board.set_color_square(self.selection)
