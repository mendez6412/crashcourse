import random


def get_secret_number():
    return random.randint(1, 10)


def get_guess():
    return int(input("Please make a guess: "))


def is_playing_again():
    playing = input("Would you like to play again? (y/n)")
    if playing == "y":
        return True


def main():
    secret_number = get_secret_number()
    # guess = get_guess()
    guesses = 0
    print("SECRET: " + str(secret_number))
    while guesses < 3:
        guess = get_guess()
        guesses += 1
        if guess == secret_number:
            print("You guessed it!")
            break
        else:
            print("You missed it!")
    if is_playing_again():
        main()


if __name__ == "__main__":
    main()
