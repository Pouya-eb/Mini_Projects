def is_happy_number(number: int) -> bool:
    """Checks whether a given number is happy or not.

    :param number: Input number
    :return: True if the number is a happy number, False otherwise
    """
    seen_numbers = set()
    while number != 1 and number not in seen_numbers:
        seen_numbers.add(number)
        number = sum((int(x) ** 2 for x in str(number)))

    return number == 1

if __name__ == '__main__':

    print(f'Is 19 a happy number: {is_happy_number(19)}')
    print(f'Is 2 a happy number: {is_happy_number(2)}')