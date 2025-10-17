""" print("Hello World")
# input("What is your Name?")
print("Hello " + input("What is your Name?"))

lastName = input("Whats your last name?")
print("Hi " + lastName)

print("Welcome to Band Name Generator")
city = input("What is your city name you grew up in? ")
pet = input("What is name of your first pet?") """

#print("Number of letters in your name: " + str(len(input("Enter your name"))))

print(3*3+3/3-3)

#f-strings

score=0
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")

print(6 + 4 / 2 - (1 * 2))

a = int("5") / int(2.7)
print(a)

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
individual_bill = round(((bill*(1+tip/100))/people),2)
print(f"${individual_bill}")
