# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     rgb_color = (r,g,b)
#     rgb_colors.append(rgb_color)
#
# print(rgb_colors)

import turtle as t
import random

t.colormode(255)


color_list = [(225, 159, 74), (38, 104, 150), (122, 166, 191), (158, 60, 83), (194, 160, 28), (199, 135, 157), (216, 85, 58), (168, 79, 49), (24, 135, 102), (204, 83, 110), (213, 228, 216), (122, 183, 153), (148, 29, 37), (235, 198, 103), (51, 167, 133), (232, 208, 218), (38, 162, 185), (3, 111, 94), (202, 220, 228), (28, 62, 115), (119, 112, 160), (235, 164, 181), (129, 34, 31), (25, 57, 85), (239, 162, 155), (160, 211, 200), (58, 43, 42), (62, 40, 56), (145, 208, 216)]

tim = t.Turtle()
tim.speed('fastest')
tim.penup()
tim.goto(-230, -200)

for x in range(10):
    for y in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.left(180)
    tim.forward(500)
    tim.right(90)
    tim.forward(50)
    tim.right(90)

tim.hideturtle()
screen = t.Screen()
screen.exitonclick()