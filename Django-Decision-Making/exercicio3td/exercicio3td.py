
# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    try:
        nota = float(input("Digite uma nota entre zero e dez: "))
        if 0 <= nota <= 10:
            print(f"Você digitou a nota {nota}.")
            break
        else:
            print("Valor inválido. A nota deve estar entre zero e dez.")
    except ValueError:
        print("Por favor, digite um valor numérico.")


