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
    is_guess = False
    while not is_guess:
        guess = input("Enter a single letter: ")
        if len(guess) == 1 and str.isalpha(guess):
            if check_guess(guess):
                is_guess = True
        else:
            print(f"Invalid letter. Please, enter a single alphabetical character.")


ask_for_input()


# Refactoring will be a continuous and constant process, but this is the time to really scrutinise your code.

# You can use the following list to make improvements:

# Meaningful Naming: Use descriptive names for methods and variables to enhance code readability. For example, create_list_of_website_links() over links() and use for element in web_element_list instead of for i in list
# Eliminate Code Duplication: Identify repeated code blocks and refactor them into separate methods or functions. This promotes code reusability and reduces the likelihood of bugs
# Getting stuck on this task? Click here to book a call to one of our support engineers
