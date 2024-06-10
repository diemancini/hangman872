import random

from milestone_2 import create_word_list


class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = [
            "_" for i in self.word
        ]  # list - A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
        self.num_letters = len(
            set([letter for letter in self.word.lower()])
        )  # int - The number of UNIQUE letters in the word that have not been guessed yet
        self.num_lives = num_lives  #: int - The number of lives the player has at the start of the game.
        self.word_list = word_list  # list - A list of words
        self.list_of_guesses = (
            []
        )  # list - A list of the guesses that have already been tried. Set this to an empty list initially

    def check_guess(self, letter):
        lower_letter = letter.lower()
        if lower_letter in self.word.lower():
            for i in range(len(self.word_guessed)):
                if self.word[i].lower() == letter:
                    self.word_guessed[i] = letter
            self.num_letters -= 1
            print(f"word_guessed: {self.word_guessed}")
            print(f"Good guess! {letter} is in the word.")
        else:
            self.num_lives -= 1
            print(f"Sorry, {letter} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            print(f"-" * 20)
            guess = input("Enter a single letter: ")
            if not str.isalpha(guess):
                print(f"Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.word_guessed:
                print(f"You already tried {guess} letter!")
            else:
                self.check_guess(guess)
                # break
            if self.num_letters == 0:

                break

            (
                self.list_of_guesses.append(guess)
                if guess not in self.list_of_guesses and str.isalpha(guess)
                else None
            )


player = Hangman(create_word_list())
player.ask_for_input()
