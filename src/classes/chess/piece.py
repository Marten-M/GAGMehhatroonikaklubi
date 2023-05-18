"""ChessPiece class file."""

from dataclasses import dataclass

@dataclass
class ChessPiece:
    name: str
    position: str
    height: float
    color: int