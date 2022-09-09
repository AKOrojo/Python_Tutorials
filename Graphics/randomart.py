import colorgram
import turtle as t

tim = t.Turtle()
t.colormode(255)

rgb_color = []
colors = colorgram.extract(
    "C:/Users/bkoro/OneDrive/Documents/Repos/CS50-s_Introduction_to_Programming_with_Python/Graphics/picture.jpg", 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_c = (r, g, b)
    rgb_color.append(new_c)
