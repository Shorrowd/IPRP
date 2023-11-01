lado1 = int(input("Introduza um lado: "))
lado2 = int(input("Introduza um lado: "))
lado3 = int(input("Introduza um lado: "))

if lado1 == lado2 == lado3:
    print("O triangulo é equilatero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triangulo é isósceles.") 
elif lado1 != lado2 != lado3:
    print("O triangulo é escaleno.")