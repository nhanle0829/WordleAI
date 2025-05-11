import json
import numpy as np


class WordleBaseAgent:
    def __init__(self, first_guess):
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