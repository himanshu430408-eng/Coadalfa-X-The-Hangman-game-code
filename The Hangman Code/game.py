import random

def play_hangman():
    # 1. Lists & predefined words
    word_list = ["apple", "river", "cloud", "brain", "ghost"]
    
    # 2. Random module to select a word
    target_word = random.choice(word_list)
    
    guessed_letters = []
    # 3. Limit incorrect guesses to 6
    attempts_remaining = 6
    
    print("Welcome to text-based Hangman!")
    print("Try to guess the secret word, one letter at a time.")
    
    # 4. While loop to keep the game running until attempts run out or the user wins
    while attempts_remaining > 0:
        
        # 5. Strings: Building the display word with guessed letters and underscores
        display_word = ""
        for letter in target_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
                
        print(f"\nWord: {display_word}")
        print(f"Attempts remaining: {attempts_remaining}")
        
        # Win condition check
        if "_" not in display_word:
            print("\nCongratulations! You guessed the word correctly!")
            break
            
        # Basic console input/output
        guess = input("Guess a letter: ").lower()
        
        # Input validation (ensuring it's a single alphabetical character)
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter! Try another one.")
            continue
            
        # Add the valid guess to our list
        guessed_letters.append(guess)
        
        # 6. If-else logic to handle correct vs. incorrect guesses
        if guess in target_word:
            print("Good guess!")
        else:
            print("Incorrect guess.")
            attempts_remaining -= 1
            
    # Loss condition check (loop finished and attempts reached 0)
    if attempts_remaining == 0:
        print(f"\nGame over! You've run out of attempts. The word was: {target_word}")

# Run the game
if __name__ == "__main__":
    play_hangman()