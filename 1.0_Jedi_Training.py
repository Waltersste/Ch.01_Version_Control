'''
1.0 Jedi Training (17pts)  Name:Stephen Walters


1. Define Forking (1pt): Taking a set of code from an origal source

2. Define Cloning (1pt): Making a copy of a car

3. Define Branching (1pt):

4. Define Committing (1pt): 

5. Define Merging (1pt): 

6. Define Pushing (1pt): Putting your local code into the cloud or github

7. Define Pull Request (1pt): Asking to put your code into someone else's code


8. TURTORIAL ART (10pts.)

Modify the starter code below to create your own cool drawing. 
Make sure you keep the last two lines of code!!!! 
Your first and last name must be written on your art.
The last line keeps the window open until you click to close.
Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''
import turtle

donut = turtle.Turtle()
#donut.shape('turtle')
donut.speed(100)
donut.ht() #ADD ONCE DONUT IT FINISHED

donut.dot(320, "tan")
donut.dot(240,"pink")
donut.dot(70,"white")
donut.pu()
donut.goto(0,100)
donut.dot(75,"pink")

donut.goto(100,0)
donut.dot(85,"pink")

donut.goto(-100,0)
donut.dot(85,"pink")

donut.goto(0,-100)
donut.dot(85,"pink")

donut.goto(65,-65)
donut.dot(80,"pink")

donut.goto(-65,-65)
donut.dot(80,"pink")

donut.goto(65,65)
donut.dot(80,"pink")

donut.goto(-65,65)
donut.dot(80,"pink")

donut.color("white")
donut.goto(37,89)
donut.pd()
donut.pensize(5)

'''
making sprinkles
'''

donut.color("purple")
donut.seth(122)
donut.fd(15)
donut.pu()
donut.goto(76,-94)

donut.color("yellow")
donut.pd()
donut.seth(92)
donut.fd(15)
donut.pu()
donut.goto(-60,87)

donut.color("#CCCCFF")
donut.pd()
donut.seth(43)
donut.fd(15)
donut.pu()
donut.goto(71,69)

donut.color("#E0B0FF")
donut.pd()
donut.seth(12333)
donut.fd(15)
donut.pu()
donut.goto(-96,-61)

donut.color("#E0B0FF")
donut.pd()
donut.seth(749)
donut.fd(15)
donut.pu()
donut.goto(-44,71)

donut.color("blue")
donut.pd()
donut.seth(1239)
donut.fd(15)
donut.pu()
donut.goto(-14,-85)

donut.color("#40E0D0")
donut.pd()
donut.seth(396)
donut.fd(15)
donut.pu()
donut.goto(53,-56)

donut.color("#800000")
donut.pd()
donut.seth(4312)
donut.fd(15)
donut.pu()
donut.goto(-42,-15)

donut.color("#808000")
donut.pd()
donut.seth(12345)
donut.fd(15)
donut.pu()
donut.goto(60,12)

donut.color("#87CEEB")
donut.pd()
donut.seth(-1234)
donut.fd(15)
donut.pu()
donut.goto(76,12)

donut.color("orange")
donut.pd()
donut.seth(-734)
donut.fd(15)
donut.pu()

donut.color("#FF10F0")
donut.goto(-98,0)
donut.pd()
donut.seth(-734)
donut.fd(15)
donut.pu()


donut.setpos(200,-300)
donut.pendown()
donut.pencolor('#FFD700')
donut.write('-Stephen Walters',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
