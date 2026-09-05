import random

# List of predefined words
words = ["python", "computer", "school", "hangman", "coding"]

# Randomly choose a word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
wrong_guesses = 0
max_wrong = 6

print("=== Welcome to Hangman ===")

while wrong_guesses < max_wrong:
    # Display the current progress
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if the player has guessed the whole word
    if "_" not in display:
        print("Congratulations! You guessed the word:", word)
        break

    # Get user input
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Remaining guesses:", max_wrong - wrong_guesses)

# If player loses
if wrong_guesses == max_wrong:
    print("\nGame Over!")
    print("The correct word was:", word)
