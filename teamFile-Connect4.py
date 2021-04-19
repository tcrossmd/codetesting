# Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.

import turtle


turtle.title("The Team Connect 4 Game")

pen_color = str()
pen_size = int()

#the board for connect four 
#board should be 7 x 6
turtle.setx(-350) 
turtle.right(180)
turtle.pencolor('blue')
turtle.pensize(2)
#line 1
turtle.right(90)
turtle.forward(350)
#line across
turtle.right(90)
turtle.forward(100)
#line down
turtle.right(90)
turtle.forward(350)
x=1
while x < 7:
    turtle.back(350)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(350)
    x = x + 1
    
turtle.right(90)
turtle.forward(702)
turtle.end_fill()

#squares
