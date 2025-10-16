""" with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data) """
    
""" import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for index, row in enumerate(data):
        if index == 0:
            pass
        else:
            temperatures.append(int(row[1]))

print(temperatures) """

#import pandas

#data = pandas.read_csv("weather_data.csv")
#print(data)
#print(data["temp"])
#print(type(data))

#data_dict = data.to_dict()
#print(data_dict)

#temp_list = data["temp"].to_list()
#print(temp_list)

#average = sum(temp_list)/len(temp_list)

#print(average)

#print(data["temp"].mean())
#print(data["temp"].max())
#print(data["condition"])
#print(data.condition)

#get rows
#print(data[data.day == "Monday"])
#print(data[data.temp == data.temp.max()] )

#monday = data[data.day=="Monday"]
#print(monday)

#print(monday.condition)

#fara = (monday.temp *9/5) + 32

#print(fara)

#create dataframe
#d#ata_dict = {"students":["Amy","James", "Angela"],"scores":[76,56,65]}
#print(data_dict)

##data = pandas.DataFrame(data_dict)
#data.to_csv("new_data.csv")

#print(data)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251013.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)
data_dict ={"Fur Color":["Gray", "Cinnamon", "Black"],
            "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]}
print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")