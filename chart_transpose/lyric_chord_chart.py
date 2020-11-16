from .chord import Chord
import logging

__all__ = ["LyricChordChart"]
logger = logging.getLogger(__name__)

NOTATION = {"-", "--", "—", "–"}


class LyricChordChart:
    def __init__(self, filename: str):
        with open(filename) as f:
            data = f.read()
        self._lines = data.splitlines()
        self._data = data

    def transpose(
        self, interval: int, to: str = "flat"
    ):
        lines = []
        for line in self._lines:
            if self._is_chord_line(line):
                chords = [
                    Chord(part).transpose(interval, to=to)
                    if Chord.is_chord(part)
                    else part
                    for part in line.split()
                ]
                line = " ".join(str(chord) for chord in chords)

                logger.info(f'MODIFIED: {line}')
            else:
                logger.info(f'IGNORED: {line}')
            lines.append(line)
        self._data = "\n".join(lines)

    @staticmethod
    def _is_chord_line(line: str) -> bool:
        return line.strip() and all(
            Chord.is_chord(part) or part in NOTATION for part in line.split()
        )

    def save(self, filename: str):
        with open(filename, "w") as f:
            f.write(self._data)
