"""ChessPiece class file."""

from dataclasses import dataclass

@dataclass
class ChessPiece:
    name: str
    position: str
    height: float
    color: int
    original_position: str

    def __repr__(self) -> str:
        """Represent the class when printed out."""
        return f"{'W' if self.color else 'B'}{self.name}"
