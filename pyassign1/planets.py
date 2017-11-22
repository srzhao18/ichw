import turtle
import math            
        
sun=turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.penup()
sun.goto(0,25)
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
j=[50,75,90,150,200,225]
k=[50,60,100,125,170,175]

def move(m,a,b):
    for p in range(1):
        for x in range(-a,a+1):
            g=1-x**2.0/a**2.0
            y=math.sqrt(b**2.0*g)
            m.goto(x,y)
        for u in range(-a,a+1):
            h=1-u**2.0/a**2.0
            v=math.sqrt(b**2.0*h)
            m.goto(-u,-v)
for e in range(5000):
    for r in range(0,len(t)):
        t[r].shape("circle")
        t[r].color(col[r])
        t[r].pu()
        t[r].goto(-j[r],0)
        t[r].pd()
        move(t[r],j[r],k[r])



turtle.mainloop()
    
