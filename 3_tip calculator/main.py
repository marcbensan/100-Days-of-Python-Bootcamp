print("Welcome to the tip calculator!")
bill = float(input("What was the total of the bill? $"))
tip = int(input("What % tip would you like to give? ie. 10, 12, 15? "))
ppl = int(input("How many people will split the bill? "))
total = (1+tip/100) * bill / ppl
totalamount ="{:.2f}".format(total)
print(f"Each person should pay: ${totalamount}")