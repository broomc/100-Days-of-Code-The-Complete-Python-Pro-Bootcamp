""" with open("/Users/clive/Downloads/my_file_download.txt") as file:    
    contents = file.read()
    print(contents)
 """

with open("new_file.txt", mode="w") as file:
    file.write("New Text In file")
    
    
    