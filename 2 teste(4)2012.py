x =int(input("Introduza um numero: "))
y =int(input("Introduza um numero: "))
z =int(input("Introduza um numero: "))

if x > y and y > z:
    print(x,y,z)
elif y > x and x > z:
    print(y,x,z)
elif z > x and x > y:
    print(z,x,y)
elif x > z and z > y:
    print(x,z,y)
elif y > z and z > x:
    print(y,z,x)
elif z > y and y > x:
    print(z,y,x)
elif x == y == z:
    print("Os numeros sao iguais.")