# Vikranth Pydeti                                         02-14-2025
# Lab 4  - This code contains the drawing of a polygon called Tridecagon using the Turtle module. 
#https://math.fandom.com/wiki/Tridecagon (accessed on 14 feb 2025)


import turtle

def tridecagonTurtle(s, x, y, t):
    t.penup()
    t.goto(x, y)
    t.pendown()

    angle = 360 / 13 

    for _ in range(13):
        t.forward(s)
        t.right(angle)
    
def main():
    print("Please enter the following values for the drawing of Tridecagon: ")
    s = float(input("Please enter the length of the tridecagon: "))
    x = float(input("Please enter the value x-coordinate of the initial point: "))
    y = float(input("Please enter the value of the y - coordinate of the initial point: "))

    t = turtle.Turtle()
    t.speed(5)

    tridecagonTurtle(s, x, y, t)

    turtle.done()

if __name__ == "__main__":
     main()
