import random

def validate_input(low: int, high: int, input_number: str) -> bool:
    """function for validation user input

    :param input_number: input number which should be between low and high
    :return: input is in format or not
    """    
    if not input_number.isdigit():
        print('Invalid input!')
        return False
    
    input_number = int(input_number)
    if input_number < low or input_number > high:
        print('Invalid input!')
        return False
    
    return True

def game(low: int=1, high: int=100, step: int=10):
    """function for playing number_guesser_game

    :param low: lower band of guess, defaults to 1
    :param high: higher band of guess, defaults to 100
    :param step: score decreasing ratio, defaults to 10
    """
    number = random.randint(low, high)
    score = 100

    while True:
        input_number = input(f'Enter your guess between {low} and {high} (Q/q to quit): ')

        if input_number.lower() == 'q':
            print('Goodbye!')
            break

        if not validate_input(low, high, input_number):
            continue

        input_number = int(input_number)
        if input_number == number:
            print(f'You guessed correctly! Your score is {max(score, 0)}')
            wanna_play = input('Do you want to play again? (y/n): ')
            if wanna_play == 'y':
                number = random.randint(low, high)
                score = 100
                continue
            else:
                print('Goodbye!')
                break


        elif input_number > number:
            print('You guessed too high!')
        else:
            print('You guessed too low!')
        
        score -= step

if __name__ == '__main__':
    game(1, 100, 5)