"""
CP1404 - Guessing Game for review and refactor
Some of this is "good" code, but some things are intentionally poor
This is for a code review and refactoring exercise
"""
import math
import random

MENU = "(P)lay, (S)et limit, (H)igh scores, (Q)uit: "

DEFAULT_LOW = 1
DEFAULT_HIGH = 10


def main():
    """Run a menu-driven guessing game with option to change high limit."""
    high_number = DEFAULT_HIGH
    number_of_games = 0
    print("Welcome to the guessing game")
    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "P":
            play(DEFAULT_LOW, high_number)
            number_of_games += 1
        elif choice == "S":
            high_number = set_limit(DEFAULT_LOW)
        elif choice == "H":
            high_scores()
        else:
            print("Invalid choice")
        choice = input(MENU).upper()
    print(f"Thanks for playing ({number_of_games} times)!")


def save_score(number_of_guesses, low, high):
    """Save score to scores.txt with range."""
    with open("scores.txt", "a", encoding="UTF-8") as outfile:
        print(f"{number_of_guesses}|{high - low + 1}", file=outfile)


def play(low, high):
    """Play guessing game using current low and high values."""
    secret_number = random.randint(low, high)
    number_of_guesses = 1
    guess = int(input(f"Guess a number between {low} and {high}: "))
    while guess != secret_number:
        number_of_guesses += 1
        if guess < secret_number:
            print("Higher")
        else:
            print("Lower")
        guess = int(input(f"Guess a number between {low} and {high}: "))
    print(f"You got it in {number_of_guesses} guesses.")
    if is_good_score(number_of_guesses, high - low + 1):
        print("Good guessing!")
    choice = input("Do you want to save your score? (y/N) ")
    if choice.upper() == "Y":
        save_score(number_of_guesses, low, high)
    else:
        print("Fine then.")


def set_limit(low):
    """Set high limit to new value from user input."""
    print("Set new limit")
    new_high = get_valid_number(f"Enter a new high value, above {low}: ")
    while new_high <= low:
        print("Higher!")
        new_high = get_valid_number(f"Enter a new high value, above {low}: ")
    return new_high


def get_valid_number(prompt):
    """Validator a number."""
    is_valid = False
    while is_valid:
        try:
            number = int(input(prompt))
            is_valid = True
        except ValueError:
            print("Invalid number")
    return number


def is_good_score(number_of_guesses, score_range):
    """Determines if a score is good."""
    return number_of_guesses <= math.ceil(math.log2(score_range))


def high_scores():
    """Read in scores and display with an ! if it is a good score"""
    scores = []
    with open("scores.txt", encoding="UTF-8") as in_file:
        for line in in_file:
            line = line.split("|")
            scores.append((int(line[0]), int(line[1])))
    scores.sort()
    for score in scores:
        marker = "!" if is_good_score(score[0], score[1]) else ""
        print(f"{score[0]} ({score[1]}) {marker}")


main()
