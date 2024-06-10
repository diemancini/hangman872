import random

from milestone_2 import create_word_list


class Hangman:

    def __init__(self, word_list, num_lives=5):
        """
        Parameters:
          word_guessed: list -> A list of the letters of the word, with _ for each letter not yet guessed.
                      For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_'].
                      If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
          num_letters: int -> The number of UNIQUE letters in the word that have not been guessed yet.
          num_lives: int -> The number of lives the player has at the start of the game.
          world_list: list -> A list of words.
          list_of_guesses: list -> A list of the guesses that have already been tried. Set this to an empty list initially.
        """
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for i in self.word]
        self.num_letters = len(set([letter for letter in self.word.lower()]))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def __update_num_letters(self):
        """
        Decrease number of letters when the user guesses the right letter.
        """
        self.num_letters -= 1

    def __game_finished(self):
        """
        Check if the game is over when the user win the game.
        Return True if the user already guessed all the letter in the secred word. Otherwise, the user continues the game.
        """
        if self.num_letters == 0:
            return True
        return False

    def __game_over(self):
        """
        Check if the game is over when the user loose the game.
        Return:
        True if the user does not have any lives. Otherwise, the user continues the game.
        """
        if self.num_lives == 0:
            return True
        return False

    def __is_repeated_guess(self, guess):
        """
        Check if the guess is not alread used
        Parameters:
        guess: string -> The letter that the user input it in each iteration.
        Return:
        True if the current letter is already inserted by the user. Otherwise, will insert the current letter in the list of guesses.
        """
        return True if guess in self.list_of_guesses and str.isalpha(guess) else False

    def __update_repeated_guess(self, guess):
        """
        Update the list of guesses that the user entered during the game (if the letter is not in the list)
        Parameters:
        guess: string -> The letter that the user input it in each iteration.
        """
        (
            self.list_of_guesses.append(guess)
            if guess not in self.list_of_guesses and str.isalpha(guess)
            else None
        )

    def __check_guess(self, letter):
        """
        Check if the letter is in secred word oguessf the Hangman game.
        If successed, it will decrease the number of distinct letter belongs to secred word.
        Otherwise, number of lives will be decreased.
        Parameters:
        letter: string -> The letter that the user input it in each iteration.
        """
        lower_letter = letter.lower()
        if lower_letter in self.word.lower():
            for i in range(len(self.word_guessed)):
                if self.word[i].lower() == letter:
                    self.word_guessed[i] = letter
            self.__update_num_letters()
            print(f"word_guessed: {self.word_guessed}")
            print(f"Good guess! {letter} is in the word.")
        else:
            self.num_lives -= 1
            print(f"Sorry, {letter} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        Controls the flow of the game.
        """
        while True:
            print(f"-" * 40)
            guess = input("Enter a single letter: ")
            if not str.isalpha(guess):
                print(f"Invalid letter. Please, enter a single alphabetical character.")
            elif self.__is_repeated_guess(guess):
                print(f"You already tried {guess} letter!")
            else:
                self.__check_guess(guess)

            if self.__game_finished():
                print("******* CONGRATULATIONS!!!! *******")
                break

            if self.__game_over():
                print("******* GAME OVER!!!! *******")
                break

            self.__update_repeated_guess(guess)


player = Hangman(create_word_list())
player.ask_for_input()
