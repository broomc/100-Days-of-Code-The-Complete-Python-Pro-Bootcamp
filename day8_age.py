""" def greet():
    print("Hello There")
    print("Whats Up")
greet()


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")

greet_with_name("Clive")

def life_in_weeks(age):
    years_left = 90 - age
    weeks_left = years_left*52
    print(f"You have {weeks_left} weeks left.")

life_in_weeks(55) """

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Clive","Tonna")

greet_with(location="New York", name="John")