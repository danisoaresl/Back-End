
# O programa deve calcular e apresentar a quantidade de números pares e ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
# informar o valor zero. Certifique-se de incluir validações para garantir que apenas números positivos sejam considerados na contagem e cálculos.

quantidade_pares = 0
quantidade_impares = 0

while True:
    numero = int(input("Digite um número (ou 0 para encerrar): "))

    if numero == 0:
        break

    if numero < 0:
        print("Por favor, digite apenas números positivos.")
        continue

    if numero % 2 == 0:
        quantidade_pares += 1
    else:
        quantidade_impares += 1
print(f"Quantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")

