from higher_lower_art import logo, vs
from higher_lower_data import data
import random

print(logo)

length = len(data)

game_on = True

def get_choice_A():
    get_A = random.randint(0,length)
    get_count_A = data[get_A]['follower_count']
    get_name_A = data[get_A]['name']
    get_description_A = data[get_A]['description']
    get_country_A = data[get_A]['country']
    return get_count_A, get_name_A,get_description_A,get_country_A
    

def get_choice_B():
    get_B = random.randint(0,length)
    get_count_B = data[get_B]['follower_count']
    get_name_B = data[get_B]['name']
    get_description_B = data[get_B]['description']
    get_country_B = data[get_B]['country']
    return get_count_B, get_name_B,get_description_B,get_country_B

def compare():
    if choice=='A' and count_A > count_B:
        print(f"You're right! Current Score : ")
    elif choice=='B' and count_B > count_A:
        print(f"You're right! Current Score : ")
    else:
        game_on = False
        print("You're are wrong")



while game_on:
    count_A, name_A, description_A, country_A = get_choice_A()

    print(f"Compare A: {name_A}, {description_A} from {country_A}")
    print(count_A)


    print(vs)

    count_B, name_B, description_B, country_B = get_choice_B()
    print(f"Compare B: {name_B}, {description_B} from {country_B}")
    print(count_B)

    choice = input("Who has more followers? Type 'A' or 'B' ")
        
    compare()