from turtle import position


row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
coordinates = position.split(" ")
x = int(coordinates[0])
y = int(coordinates[1])

map[x][y] = "X"


print(f"{row1}\n{row2}\n{row3}")
