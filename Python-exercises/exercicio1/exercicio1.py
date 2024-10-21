# dica do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes

## Faça um programa que peça dois números, realize as principais operações soma, subtração, multiplicação, divisão.

a = float(input("Informe primeiro número:"))
b = float(input("Informe segundo número:"))

operação = input("Digite a operação a realizar (+,-,* ou /):")

if operação == "+":
    resultado = a + b
    
elif operação == "-":
    resultado = a - b
    
elif operação == "*":
    resultado = a * b
    
elif operação == "/":
    resultado = a / b
    
else:
    print("Operação inválida!")
    resultado = 0
print("Resultado: ", resultado)