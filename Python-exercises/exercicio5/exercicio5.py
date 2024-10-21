# Escreva um programa que calcule o salário líquido. Lembrando de declarar o salário bruto e o percentual de desconto do Imposto de Renda.

# Renda até R$ 1.903,98; isento de imposto de renda;

# Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;

# Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;

# Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;

# Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.


def calcular_salario_liquido(salario_bruto):
    faixas = [
        (1903.98, 0.0),
        (2826.65, 0.075),
        (3751.05, 0.15),
        (4664.68, 0.225),
        (float('inf'), 0.275)
    ]

    imposto_renda = 0

    for faixa, aliquota in faixas:
        if salario_bruto <= faixa:
            imposto_renda = salario_bruto * aliquota
            break

    salario_liquido = salario_bruto - imposto_renda

    return salario_liquido

try:
    salario_bruto = float(input("Informe o salário bruto: "))
    salario_liquido = calcular_salario_liquido(salario_bruto)
    print(f"Salário líquido: R$ {salario_liquido:.2f}")
except ValueError:
    print("Por favor, insira um valor numérico para o salário bruto.")
