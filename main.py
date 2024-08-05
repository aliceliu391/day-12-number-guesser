from art import title
import random
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
# get random number from 1 - 100
num = random.randint(1, 100)

#introduction
print(title)
print("""Welcome to the number guessing game! 
I'm thinking of a number between 1 and 100. 
""")

# get user to choose a difficulty
valid = False
while not valid:
    ans = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if ans == "easy":
        num_guesses = 10
        valid = True
    elif ans == "hard":
        num_guesses = 5
        valid = True
    else:
        print("Invalid input, try again.")

print(f"You have {num_guesses} to guess the number. ")

win = False
while num_guesses > 0 and not win:
    num_guesses -= 1
    guess = int(input("Make a guess: "))
    
    if guess == num:
        win = True
    elif guess > num:
        print("Too high!")
    else:
        print("Too low...")
    

    print(f"You have {num_guesses} guesses left. ")
if win:
    print(f"You won, the number was {num}! You had {num_guesses} guesses left. ")
else:
    print(f"You lose... The number was {num}")
