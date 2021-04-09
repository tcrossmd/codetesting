# Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
#Tara - I am building the board. I should be finish with the board on by Sunday.

import turtle

pen_color = str()
fill_color = str()
pen_size = int()

#the board for connect four 
#board should be 7 x 6
#squares
for i in range(2):
    #turtle.goto(-210,150) #this is the first square
    turtle.penup()
    turtle.right(90)
    turtle.forward(2)
    turtle.pendown()
    
    turtle.pencolor('blue')
    turtle.pensize(5)
    #turtle.bgcolor('blue')
    turtle.fillcolor('blue')
    turtle.begin_fill()
    
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    
    turtle.end_fill()
    #circle for the board
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    
        
