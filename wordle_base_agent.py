import json
import numpy as np
import wordle


class WordleBaseAgent:
    def __init__(self, first_guess=None):
        self.first_guess = first_guess
        self.valid_words_with_freq = self.load_data()
        self.current_valid_words = list(self.valid_words_with_freq.keys())
        self.current_valid_words_index = set(range(len(self.current_valid_words)))
        self.word_index_table = self.get_word_index_table()
        self.feedback_table = self.get_feedback_table()

    @staticmethod
    def load_data():
        with open("./wordle_word_freq.json") as in_file:
            data = json.load(in_file)
        return data

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

    def play_games(self, num_games):
        game = wordle.WordleGame()
        total_attempt = 0
        game_wins = 0

        for i in range(num_games):
            print(f"Game {i + 1} ", end="\r", flush=True)
            result = self.play_single_game(game)
            if result[0]:
                game_wins += 1
                total_attempt += result[1]

            game.new_game()
            self.current_valid_words = list(self.valid_words_with_freq.keys())
            self.current_valid_words_index = set(range(len(self.current_valid_words)))

        return [game_wins, total_attempt]


    def play_single_game(self, game):
        if not self.first_guess:
            guessed_word = np.random.choice(self.current_valid_words)
        else:
            guessed_word = self.first_guess

        num_attempts = 0
        feedbacks = None
        for _ in range(6):
            feedbacks = game.guess_word(guessed_word)
            num_attempts += 1

            if feedbacks[1]:
                break

            self.get_new_valid_words(guessed_word, feedbacks[0])
            guessed_word = np.random.choice(self.current_valid_words)

        # result = "Solved" if feedbacks[1] else "Failed"
        # print(f"{result} in {num_attempts} attempts", flush=True)

        return [feedbacks[1], num_attempts]

    def get_new_valid_words(self, word, feedback):

        new_valid_words = []
        new_valid_words_index = set()
        for i, feedback_pattern in enumerate(self.feedback_table[self.word_index_table[word]]):
            if i not in self.current_valid_words_index:
                continue

            if feedback_pattern == feedback:
                new_valid_words.append(self.word_index_table[str(i)])
                new_valid_words_index.add(i)

        self.current_valid_words = new_valid_words
        self.current_valid_words_index = new_valid_words_index


if __name__ == "__main__":
    agent = WordleBaseAgent()
    agent.play_games(10)
