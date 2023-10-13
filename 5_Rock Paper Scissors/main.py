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

#Write your code below this line 👇
import random
inputt = input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors.")
player = int(inputt)
choice = [rock, paper, scissors]
ai = random.randint(0, 2)

if player == ai
  print(f"Computer chose: {ai}. Its a draw")

elif player == (0) and ai == (1)
  print(f"Computer chose: {ai}. You lose.")

elif player == (0) and ai == (2)
  print(f"Computer chose: {ai}. You win.")
elif player == (1) and ai == (0)
  print(f"Computer chose: {ai}. You win.")
elif player == (1) and ai == (2)
  print(f"Computer chose: {ai}. You lose.")
elif player == (2) and ai == (0)
  print(f"Computer chose: {ai}. You lose.")
elif player == (2) and ai == (1)
  print(f"Computer chose: {ai}. You win.")


