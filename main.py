# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     usable = (r, g, b)
#     rgb_colors.append(usable)
# print(rgb_colors)

import random
import turtle as worker
from turtle import Screen
screen = Screen()
screen.bgcolor("black")
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243),
              (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184),
              (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165),
              (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89),
              (82, 148, 129), (147, 17, 19), (27, 68, 102),
              (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102)
              ]


worker.hideturtle()
worker.colormode(255)
worker.shape("classic")
worker.setheading(225)
worker.penup()
worker.forward(350)
worker.setheading(0)


def run():
    for _ in range(10):

        worker.dot(20, random.choice(color_list))
        worker.penup()
        worker.forward(50)

    worker.left(90)
    worker.forward(50)
    worker.left(90)
    worker.forward(500)
    worker.right(180)


for _ in range(10):
    run()

view = Screen()
view.exitonclick()
