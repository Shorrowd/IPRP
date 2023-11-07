import turtle as t

# “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
def andar(forma,x,y):
    t.shape(forma)
    t.right(y)
    t.forward(x)
    
andar("classic",100,0)
andar("circle",100,60)
andar("arrow",100,60)
andar("turtle",100,60)
andar("square",100,60)
andar("triangle",100,60)