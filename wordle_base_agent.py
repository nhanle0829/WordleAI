class WordleBaseAgent:
    def __init__(self, first_guess):
        self.first_guess = first_guess
        self.valid_words = self.get_valid_words()

    @staticmethod
    def get_valid_words():
        with open("./wordle-answers-alphabetical.txt") as in_file:
            words = [word.strip() for word in in_file.readlines()]
        return words