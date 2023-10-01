print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
fname = (name1).lower()
sname = (name2).lower()
dick = fname.count("t") + fname.count("r") + fname.count("u") + fname.count("e") + sname.count("t") + sname.count("r") + sname.count("u") + sname.count("e")
pussy = fname.count("l") + fname.count("o") + fname.count("v") + fname.count("e") + sname.count("l") + sname.count("o") + sname.count("v") + sname.count("e") 
score = int(f"{dick}{pussy}")

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

        







