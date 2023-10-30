import turtle as t 

def estrela():
   for i in range(20):
    t.forward(200-i*10)
    t.right(144)
    
estrela()
t.exitonclick()