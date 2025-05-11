import json
import numpy as np
import wordle


class WordleBaseAgent:
    def __init__(self, first_guess=None):
        self.first_guess = first_guess
        self.valid_words = self.get_valid_words()
        self.word_index_table = self.get_word_index_table()
        self.feedback_table = self.get_feedback_table()

    @staticmethod
    def get_valid_words():
        with open("./wordle-answers-alphabetical.txt") as in_file:
            words = [word.strip() for word in in_file.readlines()]
        return words

    @staticmethod
    def get_word_index_table():
        with open("./wordle_word_index_table.json") as in_file:
            words_index = json.load(in_file)
        return words_index

    @staticmethod
    def get_feedback_table():
        with open("./wordle_word_feedback_table.json") as in_file:
            feedback_table = json.load(in_file)
        return feedback_table

    def play_game(self):
        if not self.first_guess:
            guessed_word = np.random.choice(self.valid_words)
        else:
            guessed_word = self.first_guess

        game = wordle.WordleGame()
        num_attempts = 0
        feedbacks = None
        for _ in range(6):
            feedbacks = game.guess_word(guessed_word)
            num_attempts += 1

            if feedbacks[1]:
                break

            self.get_new_valid_words(guessed_word, feedbacks[0])
            guessed_word = np.random.choice(self.valid_words)

        result = "Solved" if feedbacks[1] else "Failed"
        print(f"{result} in {num_attempts} attempts")

    def get_new_valid_words(self, word, feedback):
        new_valid_words = []
        for i, feedback_pattern in enumerate(self.feedback_table[self.word_index_table[word]]):
            if feedback_pattern == feedback:
                new_valid_words.append(self.word_index_table[str(i)])
        self.valid_words = new_valid_words


if __name__ == "__main__":
    agent = WordleBaseAgent()
    agent.play_game()




