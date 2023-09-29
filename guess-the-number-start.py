#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import socket
from art import logo
from art import chtulu
end_of_game = False
result = "l"

def difficoulty_choice():
  """Chooshe the difficoulty of the game"""
  end = False
  while not end:
    player_choice = input("Choose a difficoulty: type 'easy' you get 10 guess or 'Hard' you get only 5 ")
    if player_choice.lower() == "easy":
      return 10
    elif player_choice.lower() == "hard":
      return 5
    else:
      print("Wrong choice, try again ")
      
def Guess_check(number_cpu, diff):
  """Check the guess between PC choice and Player"""
  global end_of_game
  player_guess = 0
  while diff > 0:
    try:
      player_guess = int(input(f"You heve {diff} attempt left to guess the number\n make your guess:"))
    except:
      return "error"
    if player_guess < number_cpu:
      print("Too Low")
      diff -=1
    elif player_guess > number_cpu:
      print("Too High")
      diff -=1
    elif player_guess == number_cpu:
      return "win"
      break
    else:
      return "loose"
  return "loose"  
print(logo)
print("Welcome to the game: Get the right number!!\n")
pc_name = socket.gethostname()
while not end_of_game:
  
  print(f"Hello {pc_name}, I'm thinking of a number between 1 and 100.\n")
  difficolulty = difficoulty_choice()
  Cpu_number = random.randint(1, 100)
  final_result = Guess_check(Cpu_number, difficolulty)
  if final_result == "loose":
    print(f"You've run out of guess, the number was {Cpu_number}, you loose")
    end = input("do you want to start again? press any key to continue, type 'end' to end: ")
  elif final_result == "win":
    print(f"Good, the correct number was {Cpu_number}")
    end = input("do you want to start again? press any key to continue, type 'end' to end: ")
  elif final_result == "error":
    print("cthulhu ate your chances, please try again")
    print(chtulu)
    end = input("Do you want to try to get back your chances from the Old One? press any key to continue, type 'end' to end: ")
  if end.lower() == "end":
    end_of_game = True
  else:
    end_of_game = False

  
  
   