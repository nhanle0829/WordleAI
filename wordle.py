import numpy as np


class WordleGame:
    def __init__(self):
        self.target_word = None
        pass

    @staticmethod
    def choose_target_word():
        with open("./wordle-answers-alphabetical.txt") as in_file:
            words = [word.strip() for word in in_file.readlines()]
        print(words[:10])
        return np.random.choice(words)

    def new_game(self, start_word:str=None):
        pass


if __name__ == "__main__":
    game = WordleGame()
    