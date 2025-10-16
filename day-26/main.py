# List Comprehension
numbers = [1,2,3]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Clive"      
new_name = [l for l in name]

new_range = [r*2 for r in range(1,5)]

names = ['Alex','Beth',"Caroline","Dave","Eleanor","Freddie"]

short_names = [ short for short in names if len(short) <= 4]
print(short_names)
upper_5_names = [upper.upper() for upper in names if len(upper) >= 5]
print(upper_5_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n**2 for n in numbers]
print(squared_numbers)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(n) for n in list_of_strings]
result = [n for n in numbers if n % 2 == 0]
print(result)