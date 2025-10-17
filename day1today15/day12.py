#Global variable
player_health = 10

def drink_potion():
    potion_strength= 2
    print(player_health)

#drink_potion()

def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False
    
    for i in range(2,num):
        if num % i == 0:
            return False
    
    return True

print(is_prime(73))