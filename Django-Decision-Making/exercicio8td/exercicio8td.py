
# Criar um programa em Python que solicite três números ao usuário, utilize estruturas condicionais para determinar o maior entre eles e apresente o resultado.


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

if numero1 >= numero2 and numero1 >= numero3:
    maior_numero = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    maior_numero = numero2
else:
    maior_numero = numero3

print(f"O maior número entre {numero1}, {numero2} e {numero3} é: {maior_numero}")
