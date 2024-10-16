
# Faça um programa que lê três números inteiros e os mostra em ordem crescente.



def ler_numeros():
    numero1 = int(input("Digite o primeiro número inteiro: "))
    numero2 = int(input("Digite o segundo número inteiro: "))
    numero3 = int(input("Digite o terceiro número inteiro: "))
    return numero1, numero2, numero3

def mostrar_em_ordem_crescente(numero1, numero2, numero3):
    numeros_ordenados = sorted([numero1, numero2, numero3])
    print("Números em ordem crescente:", numeros_ordenados)

if __name__ == "__main__":

    num1, num2, num3 = ler_numeros()

    mostrar_em_ordem_crescente(num1, num2, num3)