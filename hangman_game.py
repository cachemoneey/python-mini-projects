import random

def choose_random_word():
    words = ["apple", "banana", "orange", "grape", "pineapple", "watermelon", "kiwi"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
        display += " "
    return display.strip()

def hangman():
    MAX_ATTEMPTS = 6
    word = choose_random_word()
    guessed_letters = []
    attempts = 0

    print("Welcome to Hangman!")
    print("You have 6 attempts to guess the word.")

    while attempts < MAX_ATTEMPTS:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
            if set(guessed_letters) == set(word):
                print("\nCongratulations! You guessed the word:", word)
                break
        else:
            attempts += 1
            print(f"Wrong guess! Attempts left: {MAX_ATTEMPTS - attempts}")

    else:
        print("\nGame over! The word was:", word)

if __name__ == "__main__":
    hangman()