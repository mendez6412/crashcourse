import random


def get_secret_number(max_number=10):
    return random.randint(1, max_number)


def get_guess(max_number=10):
    return int(input("Choose a number between 1 and {}: ".format(max_number)))


def is_secret(guess, answer):
    if guess == answer:
        return True
    else:
        return False


def main():
    answer = get_secret_number()
    guess = get_guess()
    if is_secret(guess, answer):
        print("You win!")
    else:
        print("Try again.")

if __name__ == '__main__':
    main()
