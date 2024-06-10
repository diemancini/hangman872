# Hangman AICore Project

## Description

The purpose of this project is create a game called "Hangman (the description of the game is at the end of this section).

In order to achieve that, the main focus is learn some concepts of:

- Manipulate Classes, methods, imports, variables and validations in python
- Create a control versions of software that you've been developing with GIT and GitHub repository.

The goal of the game is:

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## Installation instructions

Follow these steps below:

- Install [python 3](https://www.python.org/downloads/) accordingly with your OS.
- Clone repository with

```
https://github.com/diemancini/hangman872/tree/main
```

## Usage instructions

Enter in the root folder that you cloned the project

- Type:

```
python milestone_4.py
```

After that, the Terminal should present a hiffen line and input a letter with a question "Enter a single letter".

Depends what type of character(s) that you entered, you must see one of these messages:

If successed:

- "Good guess! {letter} is in the word."

Otherwise:

Invalid character:

- "Invalid letter. Please, enter a single alphabetical character."

Repeated character:

- "You already tried {guess} letter!"

Letter does not match with the secred word:

- "Sorry, {letter} is not in the word."
- ""You have {self.num_lives} lives left."

## File structure of the project

```
├── hangman
│ └── hangman_Template.py
├── milestone_2.py├── __pycache__
│   └── milestone_2.cpython-38.pyc
├── milestone_3.py
├── milestone_4.py
└── README.md
```

## License information

Licenced by AICore
