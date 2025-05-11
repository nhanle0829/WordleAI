from wordfreq import word_frequency
import json


def generate_word_frequency_data():
    with open("./wordle-answers-alphabetical.txt") as in_file:
        words = [word.strip() for word in in_file.readlines()]

    frequencies = {word: word_frequency(word, 'en') for word in words}
    total = sum(frequencies.values())
    normalized_freq = {word: freq/total for word, freq in frequencies.items()}

    with open("./wordle_word_freq.json", "w") as out_file:
        json.dump(normalized_freq, out_file, indent=4)

def generate_wordle_answer_word_index():
    with open("./wordle-answers-alphabetical.txt") as in_file:
        words = [word.strip() for word in in_file.readlines()]

    words_index = dict()
    for i, word in enumerate(words):
        words_index[i] = word
        words_index[word] = i

    with open("./wordle_word_index_table.json", "w") as out_file:
        json.dump(words_index, out_file, indent=4)

def generate_feedback_look_up_table():
    with open("./wordle_word_index_table.json") as in_file:
        word_index_table = json.load(in_file)

    feedback_table = [[0] * len(word_index_table) for _ in range(len(word_index_table))]
    for word_row, i in word_index_table.items():
        if len(word_row) < 5:
            continue

        print(f"Current row: {i}")
        for word_col, j in word_index_table.items():
            if len(word_col) < 5:
                continue

            feedback_table[i][j] = generate_feedback(word_col, word_row)

    with open("./wordle_word_feedback_table.json", "w") as out_file:
        json.dump(feedback_table, out_file, indent=4)

def generate_feedback(targeted_word: str, guessed_word: str):
    feedback = [0] * len(guessed_word)
    target_word, guessed_word = list(targeted_word), list(guessed_word)

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
    # generate_word_frequency_data()
    # generate_wordle_answer_word_index()
    # generate_feedback_look_up_table()