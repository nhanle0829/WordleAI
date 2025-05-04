import numpy as np


class WordleGame:
    def __init__(self):
        self.target_word = self.choose_target_word()
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




if __name__ == "__main__":
    game = WordleGame()
