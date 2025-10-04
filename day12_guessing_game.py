# 5, 10
import random

print("Welcome to the Guessing Game!")
print("I'm thinking of a number 1 and 100 ")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard' ")

target = random.randint(1,100)
game_on = True

print(target)

if difficulty=='easy':
    attempts = 10
    print(f"You have { attempts } attempts remaining to guess the number")
elif difficulty=='hard':
    attempts = 5
    print(f"You have { attempts }  attempts remaining to guess the number")


while game_on:
    guess = int(input("Make a guess: "))
    if guess == target:
        print("You guessed Correctly, You Win ")
        game_on = False
    elif guess < target:
        print("Too Low")
        print("Guess Again")
        attempts -= 1
        if attempts <= 0:
            print("No attempts left . You Lose . Game Over")
            game_on = False
        else: 
            print(f"You have { attempts } attempts remaining to guess the number")
    elif guess > target:
        print("Too High")
        print("Guess Again")
        attempts -= 1
        if attempts <= 0:
            print("No attempts left . You Lose . Game Over")
            game_on = False
        else: 
            print(f"You have { attempts } attempts remaining to guess the number")

    
