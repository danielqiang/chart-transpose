from pychord import Chord as _Chord

__all__ = ["Chord"]


class Chord(_Chord):
    """pychord.Chord class with improved API"""

    def transpose(self, interval: int, to: str = "flat"):
        if to == "flat":
            super().transpose(interval)
        elif to == "sharp":
            super().transpose(interval, "D")
        else:
            raise ValueError("`to` must be either 'flat' or 'sharp'.")
        return self

    @classmethod
    def is_chord(cls, chord: str):
        try:
            cls(chord)
            return True
        except ValueError:
            return False
