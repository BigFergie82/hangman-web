"""Load curated word lists once, and select words only on the server."""
from pathlib import Path
import re
import secrets


class WordManager:
    difficulties = ("easy", "medium", "hard")

    def __init__(self, directory=None):
        directory = Path(directory) if directory else Path(__file__).parent / "words"
        self._words = {}
        for difficulty in self.difficulties:
            words = []
            for line in (directory / f"{difficulty}.txt").read_text(encoding="utf-8").splitlines():
                word = line.strip().lower()
                if not word:
                    continue
                if not re.fullmatch(r"[a-z]+", word):
                    raise ValueError(f"Invalid word in {difficulty} list: {word!r}")
                if word not in words:
                    words.append(word)
            if not words:
                raise ValueError(f"The {difficulty} word list is empty.")
            self._words[difficulty] = tuple(words)

    def random_word(self, difficulty):
        if not isinstance(difficulty, str) or difficulty not in self._words:
            raise ValueError("Difficulty must be easy, medium, or hard.")
        return secrets.choice(self._words[difficulty])
