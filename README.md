# WordleGuesser
A personal attempt at making a Wordle guesser using my own knowledge of python and what I learned from watching tutorials.

# Requirements
This program requires Python 3.x to be installed on your computer.

# Usage
Clone the repository or download the source code
Run the program using the command python wordle_guesser.py
The program will make its best guess for the correct word in the game Wordle based on a list of possible 5-letter words.
Enter feedback on the guess in the format "a _ _ _ e", where each underscore represents a letter that is not correct and each letter represents a letter that is correct. The program will adjust its guess based on the feedback and continue until it guesses the correct word or until the user decides to exit the program.

# Customization
The program reads the list of possible words from a text file called word_list.txt. If you want to use a different list of words, you can replace the contents of this file with your own list of 5-letter words.

The word list I used was taken from https://gist.github.com/cfreshman/a7b776506c73284511034e63af1017ee.
Keep in mind this list could now be outdated.

# License
This program is released under the MIT License. See the LICENSE file for more information.
