"""Pure Python Hangman rules. No Flask or browser dependencies."""
import re


class GuessError(ValueError):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code


class HangmanGame:
    max_incorrect = 6

    def __init__(self, word):
        if not isinstance(word, str) or not re.fullmatch(r"[a-zA-Z]+", word):
            raise ValueError("Words must contain ASCII letters only.")
        self._word = word.lower()
        self._guesses = []

    @property
    def incorrect_letters(self):
        return [letter for letter in self._guesses if letter not in self._word]

    @property
    def remaining_guesses(self):
        return self.max_incorrect - len(self.incorrect_letters)

    @property
    def status(self):
        if all(letter in self._guesses for letter in self._word):
            return "won"
        return "lost" if self.remaining_guesses == 0 else "playing"

    def guess(self, letter):
        if self.status != "playing":
            raise GuessError("This game has ended. Start a new game.", "game_over")
        if not isinstance(letter, str) or not re.fullmatch(r"[a-zA-Z]", letter):
            raise GuessError("Guess one letter from A to Z.", "invalid_letter")
        letter = letter.lower()
        if letter in self._guesses:
            raise GuessError("That letter has already been guessed.", "duplicate_guess")
        self._guesses.append(letter)
        return self.public_state()

    def public_state(self):
        state = {
            "pattern": " ".join(letter if letter in self._guesses else "_" for letter in self._word),
            "guessed_letters": list(self._guesses),
            "incorrect_letters": self.incorrect_letters,
            "remaining_guesses": self.remaining_guesses,
            "max_incorrect": self.max_incorrect,
            "status": self.status,
        }
        if self.status != "playing":
            state["word"] = self._word
        return state
