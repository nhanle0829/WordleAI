from typing import List

import numpy as np


class WordleGame:
    def __init__(self):
        self.target_word = self.choose_target_word()
        self.num_attempt = 0
        pass

    @staticmethod
    def choose_target_word() -> str:
        with open("./wordle-answers-alphabetical.txt") as in_file:
            words = [word.strip() for word in in_file.readlines()]
        print(words[:10])
        return np.random.choice(words)

    def new_game(self, start_word:str=None):
        self.target_word = self.choose_target_word()
        if start_word is not None:
            pass

    def guess_word(self, word) -> list[list[int] | bool]:
        self.num_attempt += 1
        feedback = [0] * 5

        for i, c in enumerate(word):
            if c == self.target_word[i]:
                feedback[i] = 2
            elif c in self.target_word:
                feedback[i] = 1
            else:
                feedback[i] = 0

        correct = (feedback == [2,2,2,2,2])
        return [feedback, correct]


if __name__ == "__main__":
    game = WordleGame()
    first_guest = input()
    while not game.guess_word(first_guest)[1]:
        guess = input()
        game.guess_word(guess)
