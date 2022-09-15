with open("CSV/226 weather-data.csv") as file:
    data = file.readlines()
    print(data)

import csv

with open("CSV/226 weather-data.csv") as file:
    data = csv.reader(file)
    temp = []
    for row in data:
        if row[1] != "temp":
            temp.append(int(row[1]))

    print(temp)

import pandas

data = pandas.read_csv("CSV/226 weather-data.csv")
print(data["temp"])
print(data["temp"].max())

temp_list = data["temp"].to_list()
avg = sum(temp_list)/len(temp_list)
print(avg)

print(data[data.day == "Monday"])
