from wordle_base_agent import WordleBaseAgent


def evaluate_agents():
    agents = [WordleBaseAgent]
    total_game = 10_000

    for agent_name in agents:
        agent = agent_name()
        result = agent.play_games(total_game)
        print(str(agent_name))
        print(f"Wins: {result[0]} Total Attempt: {result[1]}")


if __name__ == "__main__":
    evaluate_agents()