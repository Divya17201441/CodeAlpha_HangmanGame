import random

def hangman():
    words = ['python', 'hangman', 'programming', 'developer', 'algorithm']
    word_to_guess = random.choice(words).lower()
    guessed_word = ['_'] * len(word_to_guess)
    guessed_letters = set()
    max_attempts = 6
    attempts = 0

    print("Welcome to Hangman!")
    print(f"The word has {len(word_to_guess)} letters: {' '.join(guessed_word)}")

    while attempts < max_attempts and ''.join(guessed_word) != word_to_guess:
        guess = input("\nGuess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input! Please enter a single alphabet.")
            continue
        
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts += 1
            print(f"Attempts remaining: {max_attempts - attempts}")

        print(" ".join(guessed_word))
    
    if ''.join(guessed_word) == word_to_guess:
        print("\nCongratulations! You've guessed the word correctly!")
    else:
        print(f"\nGame over! The word was '{word_to_guess}'.")

# Run the game
hangman()
