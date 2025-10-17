def calculate_love_score(name1,name2):
    concat_name = (name1+name2).lower()
    print(concat_name)
    true_count=0
    love_count=0
    for true_letter in concat_name:
       print(true_letter)
       if true_letter == "t" or true_letter == "r" or true_letter == "u" or true_letter == "e":
           true_count += 1
       print(f"{true_letter} True Score = {true_count}")
       
    love_count=0
    for love_letter in concat_name:
       print(love_letter)
       if love_letter == "l" or love_letter == "o" or love_letter == "v" or love_letter == "e":
           love_count += 1
       print(f"{love_letter} L Score = {love_count}")

    print(f"Love Score = {int(str(true_count) + str(love_count))}")

calculate_love_score("Kanye West","Kim Kardashian")