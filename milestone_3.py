from milestone_2 import choice_word


word = choice_word()


def check_guess(guess):
    lower_case_guess = guess.lower()
    if lower_case_guess in word:
        print(f"Good guess! {lower_case_guess} is in the word.")
        return True
    else:
        print(f"Sorry, {lower_case_guess} is not in the word. Try again.")
        return False


def ask_for_input():
    while True:
        guess = input("Enter a single letter: ")
        if len(guess) == 1 and str.isalpha(guess):
            if check_guess(guess):
                break
        else:
            print(f"Invalid letter. Please, enter a single alphabetical character.")


ask_for_input()
