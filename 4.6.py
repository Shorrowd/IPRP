a = 10
b = a

id_a = id(a)
id_b = id(b)

type_a = type(a)
type_b = type(b)

print(id_a,id_b)
print(type_a,type_b)

a = 11

id_a = id(a)
type_a = type(a)
print(id_a,type_a)
print("Os objetos são diferentes.")