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


if __name__ == "__main__":
    generate_word_frequency_data()