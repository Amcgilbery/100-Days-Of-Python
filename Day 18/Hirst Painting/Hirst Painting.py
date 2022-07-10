import turtle as t
import random
import colorgram


tim = t.Turtle()
t.colormode(255)

color_list = ((189, 157, 37), (170, 84, 47), (202, 149, 169), (129, 183, 162), (138, 178, 193), (211, 94, 64),
              (228, 168, 190), (236, 209, 221), (202, 218, 229), (215, 229, 223), (159, 67, 81), (190, 88, 102),
              (220, 198, 122), (237, 171, 158), (66, 120, 82), (59, 109, 143), (80, 161, 125), (159, 208, 194),
              (157, 206, 214), (155, 31, 18), (180, 187, 213), (154, 28, 39), (75, 152, 167), (22, 97, 38),
              (104, 121, 165), (84, 86, 18), (84, 46, 14), (24, 69, 35))

def painting():
    loop = 0
    y_coord = 0
    while loop <= (10):
        loop += 1
        for i in range(10):
            tim.dot(20, random.choice(color_list))
            tim.penup()
            tim.forward(50)
        if y_coord <= 500:
            tim.setposition(0, y_coord)
            y_coord += 50
            tim.hideturtle()


painting()

screen = t.Screen()
screen.exitonclick()
