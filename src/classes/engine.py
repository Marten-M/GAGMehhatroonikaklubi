"""ChessEngine class file."""

from chess.engine import SimpleEngine


class ChessEngine(object):
    def __init__(self, engine_path: str, level: int):
        """
        Initialize chess engine.

        :param engine_path: path to chess engine to use
        :param level: level of the chess engine to play against.
        """
        self.engine = SimpleEngine.popen_uci(engine_path)
        self.engine.configure({"Skill Level": level})
