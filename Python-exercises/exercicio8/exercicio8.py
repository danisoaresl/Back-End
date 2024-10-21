# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.


try:
    valor_por_hora = float(input("Informe quanto você ganha por hora: "))
    horas_trabalhadas = float(input("Informe o número de horas trabalhadas no mês: "))

    salario_total = valor_por_hora * horas_trabalhadas

    print(f"O total do seu salário no mês é: R$ {salario_total:.2f}")
except ValueError:
    print("Por favor, insira valores numéricos válidos.")