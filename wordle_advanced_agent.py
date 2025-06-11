from wordle_base_agent import WordleBaseAgent
import numpy as np

class WordleAdvancedAgent(WordleBaseAgent):
    def __init__(self, first_guess=None):
        super().__init__(first_guess)

    def play_single_game(self, game):
        guessed_list = []

        if not self.first_guess:
            guessed_word = np.random.choice(self.current_valid_words)
        else:
            guessed_word = self.first_guess

        num_attempts = 0
        feedbacks = None
        for _ in range(6):
            guessed_list.append(guessed_word)
            feedbacks = game.guess_word(guessed_word)
            num_attempts += 1

            if feedbacks[1]:
                break

            self.get_new_valid_words(guessed_word, feedbacks[0])
            guessed_word = self.choose_next_guess()

        return [feedbacks[1], num_attempts, guessed_list]

    def choose_next_guess(self):
        words_entropies = dict()

        for chosen_word in self.current_valid_words:
            feedbacks_probability = dict()
            total_probability = 0.0
            for target_word in self.current_valid_words:
                feedback = str(self.feedback_table[self.word_index_table[chosen_word]][self.word_index_table[target_word]])
                if feedback not in feedbacks_probability:
                    feedbacks_probability[feedback] = 0.0
                word_freq = self.valid_words_with_freq[target_word]
                feedbacks_probability[feedback] += word_freq
                total_probability += word_freq
            words_entropies[chosen_word] = self.entropy(list(feedbacks_probability.values()), total_probability)
        return max(words_entropies, key=words_entropies.get)

    @staticmethod
    def entropy(unnormalized_data, total):
        data = np.array(unnormalized_data, dtype=np.float64)

        prob_dist = data / total
        prob_dist = prob_dist[prob_dist > 0]

        return -np.sum(prob_dist * np.log2(prob_dist))

if __name__ == "__main__":
    a = WordleAdvancedAgent()
    b = a.choose_next_guess()
    print(b)