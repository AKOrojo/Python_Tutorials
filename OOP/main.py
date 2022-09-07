import turtle
import prettytable

timmy = turtle.Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("brown")
timmy.forward(100)

my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

table = prettytable.PrettyTable()
table.add_column("Pokemon", ["Bonebrush", "Pika", "Pikachu"])
table.add_column("Type", ["Psyshic", "Electric", "Electric"])
table.align = "l"
print(table)
