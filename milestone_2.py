import random


def create_word_list():
    return ["Avocado", "Mango", "Banana", "Grape", "Orange"]


def choice_word():
    return random.choice(create_word_list())


def input_letter():
    guess = input("Enter a single letter: ")
    if len(guess) == 1 and str.isalpha(guess):
        print(f"Good guess!")
    else:
        print(f"Oops! That is not a valid input.")
