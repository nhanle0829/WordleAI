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
    pass

def generate_feedback_look_up_table():
    pass

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
    generate_word_frequency_data()