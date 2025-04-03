import random

# ASCII Art below

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Python List for ASCII Art

game_images = [rock, paper, scissors]

# Defining user and computer

user_input = int(input("Rock is 0, Paper is 1, Scissors is 2. Which do You choose? \n"))
if user_input in range(0, 3):
    print(game_images[user_input])
computers_choice = random.randint(0, 2)
print(f"Computer choose {computers_choice}")
print(game_images[computers_choice])

# Game Logic below

if user_input >= 3 or user_input < 0:
    print("You typed in an invalid number. You Lose!")
elif user_input == 0 and computers_choice == 2:
    print("You Win!")
elif computers_choice == 0 and user_input == 2:
    print("You Lose!")
elif user_input > computers_choice:
    print("You Win!")
elif computers_choice > user_input:
    print("You Lose!")
elif computers_choice == user_input:
    print("It's a Draw!")
# End
