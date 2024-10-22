import random

class RockPaperScissors:
    """Main class for the rock, paper, scissors game
    """    
    def __init__(self) -> None:
        self.choices = ['rock', 'paper', 'scissors']

    def get_computer_choice(self) -> str:
        """Method to select computer's choice

        :return: computer's choice
        """
        return random.choice(self.choices)
    
    def get_player_choice(self) -> str:
        """Method to get player's choice

        :return: player's choice
        """        
        player_choice = input('Enter your choice (rock/paper/scissors): ').lower()
        if player_choice in self.choices:
            return player_choice
        else:
            print('Invalid input. Please make sure your choice is in "rock" "paper" "scissors"')
            return self.get_player_choice()
        
    def choose_winner(self, player_choice: str, computer_choice: str) -> str:
        """Method for finding the winner based on  rules

        :param player_choice: player's choice
        :param computer_choice: computer's choice
        :return: message for showing winner
        """        
        win_combination = [('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')]

        if computer_choice == player_choice:
            return 'It\'s a Tie'
        elif (player_choice, computer_choice) in win_combination:
            return 'Congratulations, you won!'
        else:
            return 'Oh no, the computer won!'
        
    def play(self) -> None:
        """Main method for playing the game
        """        
        computer_choice = self.get_computer_choice()
        player_choice = self.get_player_choice()
        print(f'Computer\'s choice: {computer_choice}')
        print(f'Your choice: {player_choice}')

        print(self.choose_winner(player_choice, computer_choice))

if __name__ == '__main__':
    game = RockPaperScissors()

    while True:
        game.play()
        continue_game = input('Do you want to play again? (Enter any key to continue or \'q\' to quit): ')
        if continue_game.lower() == 'q':
            break
