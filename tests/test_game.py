import string
import tempfile
import unittest
from pathlib import Path
from game import HangmanGame, GuessError
from word_manager import WordManager


class GameTests(unittest.TestCase):
    def test_correct_guess_reveals_all_occurrences(self):
        game = HangmanGame("apple")
        state = game.guess("P")
        self.assertEqual(state["pattern"], "_ p p _ _")
        self.assertEqual(state["remaining_guesses"], 6)
        self.assertNotIn("word", state)

    def test_miss_and_duplicate_do_not_spend_extra_lives(self):
        game = HangmanGame("apple")
        game.guess("z")
        before = game.public_state()
        with self.assertRaises(GuessError):
            game.guess("Z")
        self.assertEqual(before, game.public_state())

    def test_invalid_guesses_do_not_mutate(self):
        for value in [None, 1, True, [], {}, "", "ab", "3", " ", " a", "é", "\n"]:
            with self.subTest(value=value):
                game = HangmanGame("apple")
                before = game.public_state()
                with self.assertRaises(GuessError):
                    game.guess(value)
                self.assertEqual(before, game.public_state())

    def test_win_and_no_more_guesses(self):
        game = HangmanGame("apple")
        for letter in "aple":
            state = game.guess(letter)
        self.assertEqual(state["status"], "won")
        self.assertEqual(state["word"], "apple")
        with self.assertRaises(GuessError):
            game.guess("z")

    def test_six_misses_end_game(self):
        game = HangmanGame("apple")
        for letter in "zyxwvu":
            state = game.guess(letter)
        self.assertEqual(state["status"], "lost")
        self.assertEqual(state["remaining_guesses"], 0)
        self.assertEqual(state["word"], "apple")
        with self.assertRaises(GuessError):
            game.guess("a")

    def test_state_is_a_copy(self):
        game = HangmanGame("apple")
        game.public_state()["guessed_letters"].append("a")
        self.assertEqual(game.public_state()["guessed_letters"], [])

    def test_invalid_words(self):
        for word in ["", "two words", "a-b", None, 3, "é"]:
            with self.assertRaises(ValueError):
                HangmanGame(word)


class WordTests(unittest.TestCase):
    def test_all_difficulties(self):
        manager = WordManager()
        for difficulty in manager.difficulties:
            for _ in range(20):
                word = manager.random_word(difficulty)
                self.assertTrue(word and set(word) <= set(string.ascii_lowercase))

    def test_invalid_difficulty(self):
        manager = WordManager()
        for difficulty in ["expert", "Easy", None, [], 3]:
            with self.assertRaises(ValueError):
                manager.random_word(difficulty)

    def test_loading_normalizes_and_deduplicates(self):
        with tempfile.TemporaryDirectory() as directory:
            for difficulty in WordManager.difficulties:
                Path(directory, difficulty + ".txt").write_text(" APPLE\napple\n\n", encoding="utf-8")
            manager = WordManager(directory)
            self.assertEqual(manager._words["easy"], ("apple",))

    def test_invalid_or_empty_list_rejected(self):
        for text in ["", "not-valid"]:
            with tempfile.TemporaryDirectory() as directory:
                Path(directory, "easy.txt").write_text(text, encoding="utf-8")
                with self.assertRaises(ValueError):
                    WordManager(directory)


if __name__ == "__main__":
    unittest.main()
