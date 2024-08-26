from art import logo
import random

NUMBER=random.randint(1,100)

def take_a_guess():
    guess=int(input("Make a guess: "))
    if guess==NUMBER:
        print(f"You got it! The answer was {guess}.")
        return 0
    elif guess>NUMBER:
        print("Too high.")
        return 1
    else:
        print("Too low.")
        return -1

print(logo)
mode=input("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': """).lower()
print(NUMBER)
if mode=="easy":
    lives=10
else:
    lives=5
print(f"You have {lives} attempts remaining to guess the number.")

game_over=False
while not game_over:
    result=take_a_guess()
    if result==0:
        game_over=True
    else:
        lives-=1
        if lives>0:
            print(f"""Guess again.  
You have {lives} attempts remaining to guess the number.""")
        else:
            game_over=True
            print("You've run out of guesses, you lose.")
            print(f"The answer was {NUMBER}.")