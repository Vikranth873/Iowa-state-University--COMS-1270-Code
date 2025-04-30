# Vikranth Pydeti                                         02-22-2025
# Lab 5 - This code contains the drawing of a polygon called Tridecagon using the Turtle module, but instead of 
# drawing 1 we can draw multiple Tridecagons.

import turtle

def tridecagonTurtle(s, x, y, t):
    t.penup()
    t.goto(x, y)
    t.pendown()

    angle = 360 / 13 

    for _ in range(13):
        t.forward(s)
        t.right(angle)
    
def drawMultipleTridecagons(s, x, y, nr, sr,t):
    for i in range(nr):
        tridecagonTurtle(s, x + (i * sr), y, t)
    
def main():

    print("Please enter the following values for the drawing of Tridecagon: ")

    s = float(input("Please enter the length of the tridecagon: "))
    x = float(input("Please enter the value x-coordinate of the initial point: "))
    y = float(input("Please enter the value of the y - coordinate of the initial point: "))
    nr = int(input("Please enter the number of Tridecagons that you would like to draw: "))
    sr = float(input("Enter the space that you prefere between the tridecagons: "))

    screen = turtle.Screen()
    screen.title("Multiple Tridecagon Drawerer")
    t = turtle.Turtle()
    t.speed(5)

    drawMultipleTridecagons(s, x, y, nr, sr, t)

    turtle.done()

if __name__ == "__main__":
    main()