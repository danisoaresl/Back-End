
# Faça um programa que peça dois números e imprima o maior deles.


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    maior_numero = numero1
else:
    maior_numero = numero2

print("O maior número é:", maior_numero)