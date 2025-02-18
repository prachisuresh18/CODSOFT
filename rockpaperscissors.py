import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


game_images = [rock, paper, scissors]
user_score = 0
computer_score = 0
play_again = "yes"

while play_again == "yes":
    user_choice = (int)(input("What do you choose? Type 0 for 'rock', type 1 for 'paper' and type 2 for 'scissors'\n"))

    if user_choice >= 0 and user_choice <= 2:
        print("You chose:", game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:", game_images[computer_choice])

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number. You lose!")

    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
        user_score += 1
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
        computer_score += 1
    elif computer_choice > user_choice:
        print("You lose!")
        computer_score += 1
    elif user_choice > computer_choice:
        print("You win!")
        user_score += 1
    elif computer_choice == user_choice:
        print("It's a draw!.")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

print(f"You scored {user_score} \nComputer scored {computer_score }")

if user_score > computer_score:
    print("YOU ARE A STAR ...YOU WIN THE GAME !!!")
else:
    print("You lose this game! :( But don't give up! Try again and beat the computer!")
