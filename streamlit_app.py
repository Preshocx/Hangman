import streamlit as st
import random

# List of words for the game
words = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry']

def main():
    st.title("Hangman Game")
    st.write("Welcome to the Hangman Game!")
    st.write("Guess the letters to reveal the hidden word.")

    # Get a random word from the list
    word = random.choice(words)

    # Initialize the game state
    guessed_letters = []
    num_guesses = 0

    # Display the initial hidden word
    hidden_word = hide_word(word, guessed_letters)
    st.subheader("Hidden Word:")
    st.write(hidden_word)

    # User input field for guessing letters
    user_input = st.text_input("Enter a letter")

    if user_input:
        # Process the user's guess
        guess = user_input.lower()

        if guess.isalpha() and len(guess) == 1:
            # Check if the letter has already been guessed
            if guess in guessed_letters:
                st.warning("You have already guessed that letter.")
            else:
                # Add the letter to the guessed letters
                guessed_letters.append(guess)

                # Check if the letter is in the word
                if guess in word:
                    st.success("Correct guess!")
                else:
                    st.error("Wrong guess!")

                # Increment the number of guesses
                num_guesses += 1

        else:
            st.warning("Please enter a single letter.")

    # Update the hidden word
    hidden_word = hide_word(word, guessed_letters)

    # Display the updated hidden word
    st.subheader("Hidden Word:")
    st.write(hidden_word)

    # Check if the game is won or lost
    if hidden_word == word:
        st.success("Congratulations! You won the game.")
    elif num_guesses >= 6:
        st.error("Sorry, you lost the game. The word was: " + word)

    # Play again button
    if st.button("Play Again"):
        main()

def hide_word(word, guessed_letters):
    # Replace unguessed letters with underscores
    hidden_word = ""
    for letter in word:
        if letter in guessed_letters:
            hidden_word += letter
        else:
            hidden_word += "_"
    return hidden_word

if __name__ == '__main__':
    main()
