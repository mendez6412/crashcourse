import random


def get_secret_number():
    return random.randint(1, 10)


def get_guess():
    return int(input("Please make a guess: "))


def main():
    secret_number = get_secret_number()
    guess = get_guess()
    print("SECRET: " + str(secret_number))
    print("GUESS: " + str(guess))
    if guess == secret_number:
        print("You guessed it!")
    else:
        print("You missed it!")


if __name__ == "__main__":
    main()
