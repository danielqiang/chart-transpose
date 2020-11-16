from .chord import Chord
from .lyric_chord_chart import LyricChordChart

import logging

WHITE = "\033[1m"
logging.basicConfig(
    level=logging.INFO, format=WHITE + "%(levelname)s: [%(name)s] %(message)s"
)
