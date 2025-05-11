from wordle_base_agent import WordleBaseAgent
import json
import numpy as np

class WordleIntermediateAgent(WordleBaseAgent):
    def __init__(self, first_guess=None):
        super().__init__(first_guess)

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
            valid_words = sorted(self.current_valid_words, key=lambda word:self.valid_words_with_freq[word], reverse=True)
            guessed_word = valid_words[0]

        # result = "Solved" if feedbacks[1] else "Failed"
        # print(f"{result} in {num_attempts} attempts", flush=True)

        return [feedbacks[1], num_attempts]