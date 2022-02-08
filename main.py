import random

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



question = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))


options = ["rock", "paper", "scissors"]
pictures = [rock, paper, scissors]


numberList = [0,1,2]
computer_Numberical_Choice = random.choice(numberList)
computerChoice = options[computer_Numberical_Choice]
humanChoice = options[question]

if (computerChoice == "rock") and (humanChoice == "scissors"):
  print(f"{pictures[question]}\nComputer chose:\n{pictures[computer_Numberical_Choice]}\nYou Lose")
elif (computerChoice == "paper") and(humanChoice == "rock"):
  print(f"{pictures[question]}\nComputer chose:\n{pictures[computer_Numberical_Choice]}\nYou Lose")
elif (computerChoice == "scissors") and(humanChoice == "paper"):
  print(f"{pictures[question]}\nComputer chose:\n{pictures[computer_Numberical_Choice]}\nYou Lose")
elif (humanChoice == "rock") and(computerChoice == "scissors"):
  print(f"{pictures[question]}\nComputer chose:\n{pictures[computer_Numberical_Choice]}\nYou Win")
elif (humanChoice == "paper") and(computerChoice == "rock"):
  print(f"{pictures[question]}\nComputer chose:\n{pictures[computer_Numberical_Choice]}\nYou Win")
elif (humanChoice == "scissors") and(computerChoice == "paper"):
  print(f"{pictures[question]}\nComputer chose:\n{pictures[computer_Numberical_Choice]}\nYou Win")
elif humanChoice == computerChoice:
  print(f"Your Choice\n{pictures[question]}\nComputer chose:\n{pictures[computer_Numberical_Choice]}\nYou Drew")






