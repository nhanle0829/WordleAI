import numpy as np
import json


class WordleGame:
    def __init__(self):
        self.words = None
        self.freq = None

        self.load_data()

        self.target_word = self.choose_target_word()
        self.num_attempt = 0

    def load_data(self):
        with open("./wordle_word_freq.json") as in_file:
            data = json.load(in_file)
        self.words = list(data.keys())
        self.freq = list(data.values())

    def choose_target_word(self) -> str:
        return np.random.choice(self.words, p=self.freq)

    def set_target_word(self, word: str) -> None:
        self.target_word = word

    def new_game(self, start_word:str=None) -> None:
        self.target_word = self.choose_target_word()
        if start_word is not None:
            self.guess_word(start_word)

    def guess_word(self, word) -> list[list[int] | bool]:
        self.num_attempt += 1
        feedback = self.give_feedback(word)

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

    def give_feedback(self, guessed_word: str) -> list[int]:
        feedback = [0] * len(guessed_word)
        target_word = list(self.target_word)
        guessed_word = list(guessed_word)

        for i in range(len(target_word)):
            if target_word[i] == guessed_word[i]:
                feedback[i] = 2
                target_word[i] = '_'
                guessed_word[i] = '_'

        for i, c in enumerate(guessed_word):
            if c != '_':
                for j in range(len(target_word)):
                    if c == target_word[j]:
                        feedback[i] = 1
                        target_word[j] = '_'
                        guessed_word[i] = '_'
                        break

        return feedback


if __name__ == "__main__":
    game = WordleGame()
    # game.play_human()

    game.set_target_word("crepe")
    print(game.give_feedback("speed"))
