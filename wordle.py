import numpy as np


class WordleGame:
    def __init__(self):
        self.target_word = self.choose_target_word()
        self.num_attempt = 0

    @staticmethod
    def choose_target_word() -> str:
        with open("./wordle-answers-alphabetical.txt") as in_file:
            words = [word.strip() for word in in_file.readlines()]
        print(words[:10])
        return np.random.choice(words)

    def set_target_word(self, word: str) -> None:
        self.target_word = word

    def new_game(self, start_word:str=None) -> None:
        self.target_word = self.choose_target_word()
        if start_word is not None:
            self.guess_word(start_word)

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

    def play_human(self):
        guess = input("Enter your first guess: ")
        feedbacks = self.guess_word(guess)
        while not feedbacks[1]:
            if self.num_attempt == 6:
                print("You Lose!")
                print(f"The correct word is: {self.target_word}")
                break

            guess = input("Enter your next guess: ")
            feedbacks = self.guess_word(guess)

        if feedbacks[1]:
            print("You Win!")


if __name__ == "__main__":
    game = WordleGame()
    game.play_human()
