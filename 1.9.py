print("Introduza o peso em kilos")
peso = float(input())

print("Introduza a altura em metros")
altura = float(input())

imc_calculo = (peso/(altura**2))

print("O valor do IMC é", imc_calculo)