from wordle_base_agent import WordleBaseAgent
from wordle_intermediate_agent import WordleIntermediateAgent
from wordle_advanced_agent import WordleAdvancedAgent
from wordle import WordleGame


def evaluate_agents():
    agents = [WordleBaseAgent, WordleIntermediateAgent, WordleAdvancedAgent]
    total_game = 1_000_000

    for agent_name in agents:
        agent = agent_name("trace")
        # result = agent.play_games(total_game)
        result = agent.play_exhaustive_words()
        print(str(agent_name))
        print(f"Wins: {result[0]} Total Attempt: {result[1]} Average Guess: {result[1]/result[0]}")

def play_today_game(today_word, first_guessed):
    agents = [WordleBaseAgent, WordleIntermediateAgent, WordleAdvancedAgent]
    game = WordleGame()

    for agent_name in agents:
        game.set_target_word(today_word)
        agent = agent_name(first_guessed)

        result = agent.play_single_game(game)
        print(str(agent_name))
        if result[0]:
            print(f"Solved in {result[1]} attempts!")
        else:
            print("Failed")

        print(" -> ".join(result[2]))


if __name__ == "__main__":
    # evaluate_agents()
    play_today_game("taffy", None)