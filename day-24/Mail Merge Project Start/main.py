#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
#print("Mail Merge")
with open("Input/Names/invited_names.txt") as file:
    name_list = [line.strip() for line in file.readlines()]

#print(name_list)
letters=[]
for name in name_list:
    with open("Input/Letters/starting_letter.txt", "r") as file:
        letter = file.read()
        letters.append(letter.replace("[name]", name))

#print(letters)    

for index,letter in enumerate(letters):
    filename = f"letter_{index}"
    with open(f"Output/ReadyToSend/{filename}", "w") as file:
        file.write(letter)

