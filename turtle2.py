#Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
#>>> #	Program Name:	
#	Author:		Tara Cross
#	Date Written:	Feb. 28, 2021
#	Description: 	Turtle Lab 2
#
#	MODIFICATION LOG
#	Change # 	Date		Pgmr	Description
#	A0000002	02/28/21	CKK		Initial Install
import turtle
#circle = turtle.pen()
color = turtle.pen('red, blue, yellow')
Shape = turtle.pen('circle, square')
question = turtle.pen()
question2 = turtle.pen()
Location = turtle.pen('Top Right, Top Right, Bottom Left, Bottom Right')

#yellow = turtle.pen()
#red = turtle.pen()
shape = turtle.textinput(Shape,"What shape do you want to draw, a circle or square? ")
if shape == "circle":
        question = turtle.textinput(color,"Select a pen color: red, blue or yellow")
        location = turtle.textinput(Location,"Where do you want to draw it, Top Left, Top Right, Bottom Left or Bottom Right? ")
 
if question == "red" and location == "Top Left":
        pen_color = str()
        fill_color = str()
        pen_size = int()
        turtle.penup()
        turtle.goto(-400, 300)
        turtle.pendown()
        turtle.pensize('3')
        turtle.pencolor('red')
        turtle.fillcolor('pink')
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()

elif question == "red" and location == "Top Right":
        pen_color = str()
        fill_color = str()
        pen_size = int()
        turtle.penup()
        turtle.goto(400, 300)
        turtle.pendown()
        turtle.pensize('5')
        turtle.pencolor('red')
        turtle.fillcolor('pink')
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()
        
elif question == "red" and location == "Bottom Left":
        pen_color = str()
        fill_color = str()
        pen_size = int()
        turtle.penup()
        turtle.goto(-400, -300)
        turtle.pendown()
        turtle.pensize('7')
        turtle.pencolor('red')
        turtle.fillcolor('pink')
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()
        
elif question == "red" and location == "Bottom Right":
        pen_color = str()
        fill_color = str()
        pen_size = int()
        turtle.penup()
        turtle.goto(400, -300)
        turtle.pendown()
        turtle.pensize('9')
        turtle.pencolor('red')
        turtle.fillcolor('pink')
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()
 
if question == "blue" and location == "Top Left":
                   
        pen_color = str()
        fill_color = str()
        pen_size = int()
        turtle.penup()
        turtle.goto(-400, 300)
        turtle.pendown()
        turtle.pensize('3')
        turtle.pencolor('blue')
        turtle.fillcolor('green')
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()
  

elif question == "blue" and location == "Top Right":
        pen_color = str()
        fill_color = str()
        pen_size = int()
        turtle.penup()
        turtle.goto(400, 300)
        turtle.pendown()
        turtle.pensize('5')
        turtle.pencolor('blue')
        turtle.fillcolor('green')
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()
        
elif question == "blue" and location == "Bottom Left":
        pen_color = str()
        fill_color = str()
        pen_size = int()
        turtle.penup()
        turtle.goto(-400, -300)
        turtle.pendown()
        turtle.pensize('7')
        turtle.pencolor('blue')
        turtle.fillcolor('green')
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()
        
elif question == "blue" and location == "Bottom Right":
        pen_color = str()
        fill_color = str()
        pen_size = int()
        turtle.penup()
        turtle.goto(400, -300)
        turtle.pendown()
        turtle.pensize('9')
        turtle.pencolor('blue')
        turtle.fillcolor('green')
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()
 
       
if question == "yellow" and location == "Top Left":
                   
        pen_color = str()
        fill_color = str()
        pen_size = int()
        turtle.penup()
        turtle.goto(-400, 300)
        turtle.pendown()
        turtle.pensize('3')
        turtle.pencolor('yellow')
        turtle.fillcolor('orange')
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()
  

elif question == "yellow" and location == "Top Right":
        pen_color = str()
        fill_color = str()
        pen_size = int()
        turtle.penup()
        turtle.goto(400, 300)
        turtle.pendown()
        turtle.pensize('5')
        turtle.pencolor('yellow')
        turtle.fillcolor('orange')
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()
        
elif question == "yellow" and location == "Bottom Left":
        pen_color = str()
        fill_color = str()
        pen_size = int()
        turtle.penup()
        turtle.goto(-400, -300)
        turtle.pendown()
        turtle.pensize('7')
        turtle.pencolor('yellow')
        turtle.fillcolor('orange')
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()
        
elif question == "yellow" and location == "Bottom Right":
        pen_color = str()
        fill_color = str()
        pen_size = int()
        turtle.penup()
        turtle.goto(400, -300)
        turtle.pendown()
        turtle.pensize('9')
        turtle.pencolor('yellow')
        turtle.fillcolor('orange')
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()
 
if shape == "square":
        question2 = turtle.textinput(color,"Select a pen color for your square: red, blue or yellow")
        location = turtle.textinput(Location,"Where do you want to draw it, Top Left, Top Right, Bottom Left or Bottom Right? ")
if question2 == "red":        
      
        turtle.pencolor('red')
        turtle.fillcolor('yellow')
        turtle.begin_fill()
        turtle.penup()
        turtle.right(90)
        turtle.forward(90)
        turtle.pendown()

        
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
elif question2 == "blue" and location == "Top Left":      
       
        turtle.pencolor('blue')
        turtle.fillcolor('purple')
        turtle.begin_fill()
        
        turtle.penup()
        turtle.right(90)
        turtle.forward(90)
        turtle.pendown()

        
        turtle.right(90)
        turtle.fCIRorward(50)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(50)

        turtle.end_fill()
        
elif question2 == "yellow":       
       # turtle.pensize('3')
        turtle.pencolor('yellow')
        turtle.fillcolor('lime')
        turtle.begin_fill()
        
        turtle.penup()
        turtle.right(90)
        turtle.forward(90)
        turtle.pendown()

        
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
        turtle.pendown()
else:
        print('Shape or Color requested is not recognized, try again')