import pandas

data = pandas.read_csv("CSV/228201~1.CSV")
colour = data["Primary Fur Color"].value_counts()
print(colour)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Total": [colour[0], colour[1], colour[2]]
}

df = pandas.DataFrame(data_dict)
df.to_csv("CSV/COUNT.CSV")

print(data_dict)
