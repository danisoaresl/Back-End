# Solicite ao usuário o peso em kg e a altura em metros. Calcule e imprima o índice de Massa Corporal (IMC) usando a fórmula:
# IMC = peso / (altura x altura).

def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

peso = float(input("Informe o peso em kg: "))
altura = float(input("Informe a altura em metros: "))

imc = calcular_imc(peso, altura)

print(f"O Índice de Massa Corporal (IMC) é: {imc:.2f}")