import random

word_list = ["Avocado", "Mango", "Banana", "Grape", "Orange"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Enter a single letter: ")
if len(guess) == 1 and str.isalpha(guess):
    print(f"Good guess!")
else:
    print(f"Oops! That is not a valid input.")
