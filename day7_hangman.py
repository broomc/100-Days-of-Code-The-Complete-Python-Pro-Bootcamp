import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)


placeholder = ""
word_length = len(chosen_word)


game_over = False
correct_letters = []

while not game_over:
    display=""
    print(f"*********************************************{lives}/6 LIVES LEFT*******************************")
    guess = input("Please Guess a letter \n").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    for char in chosen_word:
        if char == guess:
            display += char
            correct_letters.append(guess)
        elif char in correct_letters:
            display += char
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You've guessed {guess}, that's not in the word. You loose a life")
        if lives == 0:
            game_over = True
            print(f"******************************IT WAS {chosen_word} . YOU LOSE**********************************")
        

    if "_" not in display:
        game_over = True
        print("*********************************YOU WIN************************************") 
 
    print(stages[lives])