# Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
# >>> #	Program Name:	
# 	Author:		Tara Cross
# 	Date Written:	Feb. 28, 2021
# 	Description: 	Turtle Lab 2

# 	MODIFICATION LOG
# 	Change # 	Date		Pgmr	Description
# 	A0000002	02/28/21	CKK		Initial Install


import turtle

#variables
pen_color = str()
fill_color = str()
pen_size = int()

#moving the pen
turtle.penup()
turtle.goto(0, 150)
turtle.pendown()

turtle.pensize('3')
turtle.pencolor('red')
turtle.fillcolor('yellow')

turtle.begin_fill()

#draw cricle
turtle.circle(50)

#stopping the fill
turtle.end_fill()

#square
turtle.penup()
turtle.right(90)
turtle.forward(90)
turtle.pendown()

turtle.pencolor('blue')
turtle.fillcolor('red')
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

#triangle
turtle.penup()
turtle.left(90)
turtle.forward(170)
turtle.pendown()

turtle.pencolor('yellow')
turtle.fillcolor('blue')
turtle.begin_fill()

turtle.right(35)
turtle.forward(125)
turtle.right(235)
turtle.forward(150)
turtle.left(127)
turtle.forward(130)

turtle.end_fill()

import time #typed in at the top
time.sleep(3)
turtle.reset()
turtle.setup(600, 600) #sets up the size of the window


 OWN MY OWN PROJECT BELOW
yellow = turtle.pen()
red = turtle.pen()

color = ['red', 'blue', 'yellow']
Shape = ['circle', 'triange', 'square']
Location = ['Top Left', 'Top Right', 'Bottom Left', 'Bottom Right']

def drawasquare(FColor, pSize, pColor):
    
    turtle.pensize(pSize)#changes
    turtle.pencolor(pColor)
    turtle.fillcolor(FColor)
    turtle.begin_fill()
          
    for side_index in range(0,4):
        turtle.left(90)
        turtle.forward(100)
        
    turtle.end_fill()
    
def drawacircle(FColor, pSize, pColor):    
    turtle.pensize(pSize)
    turtle.pencolor(pColor)
    turtle.fillcolor(FColor)
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    
    
    
def drawatriangle(FColor, pSize, pColor):    
    turtle.pensize(pSize)
    turtle.pencolor(pColor)
    turtle.fillcolor(FColor)
    turtle.begin_fill()
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.end_fill()
    
def getlocation():
    print("These are the valid locations")
    for loc_index in range(0,len(Location)): 
        print(Location[loc_index])
        
    print("")
    loc=input("Choose location")
    if loc == "TL":
        return -400,300
    elif loc == "TR":
        return 400,300
    elif loc == "BL":
        return -400,-300
    elif loc == "BR":
        return 400,-300
    
def getShape():
    print("These are the valid shapes")
    for shp_index in range(0,len(Shape)): 
        print(Shape[shp_index])
        
    print("")
    shp=input("Choose Shape")
    return shp 

def getFColor():
    print("These are the valid fill colors")
    for clr_index in range(0,len(color)): 
        print(color[clr_index])
        
    print("")
    clr=input("Choose color")
    return clr 
    
def getPColor():
    print("These are the valid pen colors")
    for clr_index in range(0,len(color)): 
        print(color[clr_index])
        
    print("")
    clr=input("Choose color")
    return clr 
    
def getPSize():
    pSize=int(input("Please enter a pen size 3 through 10"))
    return pSize

def goToSpot(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
        
        
def main():
    xpos = int()
    ypos = int()
    shp = str()  
 #   t1 = turtle()
    xpos, ypos = getlocation()
    shp = getShape()
    FColor = getFColor()
    pSize = getPSize()
    pColor = getPColor()
    
    goToSpot(xpos, ypos)
    if shp == "circle":
        drawacircle(FColor, pSize, pColor)
    elif shp == "triangle":
        drawatriangle(FColor, pSize, pColor)
    elif shp == "square":
        drawasquare(FColor, pSize, pColor)
    else:
        print("Unknown Shape")
        
        
main()
    
        