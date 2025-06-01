from wordle_base_agent import WordleBaseAgent
from wordle_intermediate_agent import WordleIntermediateAgent
from wordle_advanced_agent import WordleAdvancedAgent


def evaluate_agents():
    agents = [WordleBaseAgent, WordleIntermediateAgent, WordleAdvancedAgent]
    total_game = 1_000_000

    for agent_name in agents:
        agent = agent_name("trace")
        # result = agent.play_games(total_game)
        result = agent.play_exhaustive_words()
        print(str(agent_name))
        print(f"Wins: {result[0]} Total Attempt: {result[1]} Average Guess: {result[1]/result[0]}")


if __name__ == "__main__":
    evaluate_agents()