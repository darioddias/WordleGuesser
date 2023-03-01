import random

# Load the list of possible words from a text file
with open("word_list.txt") as f:
    word_list = [word for word in f.read().splitlines() if len(word) == 5]

# Define the number of guesses you want to make
num_guesses = 1000

# Define a dictionary to keep track of the probability of each word being correct
word_probabilities = {word: 1/len(word_list) for word in word_list}

# Define a function to get feedback on each guess
def get_feedback(guess, word):
    feedback = ["_" for _ in range(len(guess))]
    for i in range(len(guess)):
        if guess[i] == word[i]:
            feedback[i] = guess[i]
    return " ".join(feedback)

# Loop until the user exits the program
while True:
    # Get the word with the highest probability of being correct
    guess = max(word_probabilities, key=word_probabilities.get)
    
    # Print the guess
    print("Guess: {}".format(guess))
    
    # Get feedback on the guess
    feedback = input("Enter feedback on the guess (e.g. 'a _ _ _ e' means the first and fifth letters are correct): ")
    if feedback == "":
        break
    
    # Convert feedback to a list of letters
    feedback = feedback.split()
    
    # Adjust the probabilities of each word based on the feedback
    for word in word_probabilities:
        new_prob = word_probabilities[word]
        for i in range(len(guess)):
            if guess[i] != word[i]:
                new_prob *= (1 - word_probabilities[guess])
            else:
                if feedback[i] == "_":
                    new_prob *= (5 - word_probabilities[guess].count(guess[i])) / 5
                else:
                    new_prob *= (word_probabilities[guess].count(guess[i]) / 5) if feedback[i] == guess[i] else 0
        word_probabilities[word] = new_prob
    
    # Normalize the probabilities to ensure they add up to 1
    total_prob = sum(word_probabilities.values())
    for word in word_probabilities:
        word_probabilities[word] /= total_prob
    
    # Check if the correct word has been guessed
    if feedback == [guess[i] for i in range(len(guess))]:
        print("Correct!")
        break
