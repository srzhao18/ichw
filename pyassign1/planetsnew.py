import turtle
import math            
        
sun=turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.penup()
sun.goto(0,10)
sun.pendown
sun.stamp()             

mercury=turtle.Turtle()
venus=turtle.Turtle()
earth=turtle.Turtle()
mars=turtle.Turtle()
jupiter=turtle.Turtle()
saturn=turtle.Turtle()

t=[mercury,venus,earth,mars,jupiter,saturn]
col=["blue","green","purple","orange","black","red"]
j=[50,75,100,150,200,225]
k=[50,60,125,100,52,85]

def move(m,n,a,b):
    x=a*math.cos(n)
    y=b*math.sin(n)
    m.pu()
    m.goto(x,y)
    m.pd()
    m.stamp()
for s in range(8000):
    for f in range(0,361):
        for r in range(0,len(t)):
            t[r].shape("circle")
            t[r].turtlesize(1)
            t[r].color(col[r])
            move(t[r],f/40,j[r],k[r])
turtle.mainloop()
