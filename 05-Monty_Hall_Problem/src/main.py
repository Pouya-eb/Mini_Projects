import random

def monty_hall(switch_door: bool=True) -> bool:
    """Simulate a single Monty Hall Game.

    :param switch_door: if True, the player will switch the door.
    :return: True if the player wins the car, False otherwise.
    """
    doors = ['goat', 'goat', 'car']
    random.shuffle(doors)

    initial_choice = random.choice(range(3))
    doors_revealed = [i for i in range(3) if i != initial_choice and doors[i] != 'car']
    door_revealed = random.choice(doors_revealed)

    if switch_door:
        final_choice = [i for i in range(3) if i != initial_choice and i != door_revealed][0]
    else:
        final_choice = initial_choice

    return doors[final_choice] == 'car'
    

def simulate_games(num_games: int=1000) -> tuple:
    """Simulate a number of Monty Hall games.

    :param int num_games: The number of games to simulate.
    :return: number of winning games without switching vs switching
    """
    num_wins_without_switching = sum(monty_hall(switch_door=False) for _ in range(num_games))
    num_wins_with_switching = sum(monty_hall(switch_door=True) for _ in range(num_games))

    return (num_wins_without_switching, num_wins_with_switching)


if __name__ == '__main__':
    num_games = 10000
    num_wins_without_switching, num_wins_with_switching = simulate_games(num_games)
    print(f"Winning chance without switching door: {round(num_wins_without_switching / num_games * 100, 2)}%")
    print(f"Winning chance with switching door: {round(num_wins_with_switching / num_games * 100, 2)}%")