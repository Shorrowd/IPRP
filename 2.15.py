import turtle as t 

a = 0
b = 0
t.speed(20)

for i in range(20) :
    t.setheading(-60+b)
    b += 10
    for i in range(4):
        t.forward(20+a)
        t.left(90)
    a += 10
        