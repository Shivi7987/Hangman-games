import random

def hangman():
    words = ['apple', 'banana', 'grape', 'orange', 'lemon']  # Small predefined list
    word = random.choice(words)
    guessed = ['_'] * len(word)
    attempts = 6
    guessed_letters = set()

    print("Welcome to Hangman!")
    print("You have 6 incorrect guesses. Let's start!")

    while attempts > 0 and '_' in guessed:
        print("\nWord: " + ' '.join(guessed))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")

    if '_' not in guessed:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nSorry, you ran out of attempts. The word was:", word)

if __name__ == "__main__":
    hangman()