from replit import clear
import random

from hangman_words import *
from hangman_art import *
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
print(logo) 


display = []
for _ in range(word_length):
    display += "_"


while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
         print ("you've already guessed ",guess)

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print("You guessed",guess,",not in the word. You lose a life ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])