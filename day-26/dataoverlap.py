with open("file1.txt", mode="r") as file:
    number_list_1 = [line.strip() for line in file.readlines()]
    num_list_int_1 = [int(n) for n in number_list_1]
    print(num_list_int_1)

with open("file2.txt", mode="r") as file:
    number_list_2 = [line.strip() for line in file.readlines()]
    num_list_int_2 = [int(n) for n in number_list_2]
    print(num_list_int_2)
    
result = [x for x in num_list_int_1 if x in num_list_int_2 ]
print(result)