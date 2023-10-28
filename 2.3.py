import random
import turtle as t
from turtle import Screen

Screen = Screen()
Screen.colormode(255)

r = 0
g = 0
b = 0
x = 0
y = 0

def linha(x,y,r,g,b):
    for i in range(50):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        x = random.randint(0,100)
        y = random.randint(0,360)
        t.color(r,g,b)
        t.setheading(y)
        t.forward(x)
        
linha(x,y,r,g,b)
    
t.exitonclick()