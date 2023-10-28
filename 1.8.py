l = 7.62
d = 8.89
r = d/2

hamburguer_quadrado_area = l*l
hamburguer_redondo_area = (r**2)*3.1416

if hamburguer_quadrado_area > hamburguer_redondo_area:
    print("Não pode reclamar com o tamanho do novo hamburguer.")
else:
    print("Pode reclamar com o tamanho do novo hamburguer.")
    
print(hamburguer_quadrado_area)
print(hamburguer_redondo_area)
    