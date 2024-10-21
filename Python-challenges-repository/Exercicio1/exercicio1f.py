
# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

# OBS Neste exemplo, a função soma_tres_numeros recebe três argumentos (a, b e c) e retorna a soma deles. No exemplo de uso, o programa solicita
# ao usuário que insira três números, chama a função com esses números e imprime o resultado.

def soma_tres_numeros(a, b, c):
    resultado = a + b + c
    return resultado

# Exemplo de uso da função
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

resultado_soma = soma_tres_numeros(numero1, numero2, numero3)

print(f"A soma dos três números é: {resultado_soma}")