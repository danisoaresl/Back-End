
# Desenvolver um programa que solicite a idade do usuário e identifique se ele é uma criança, um adolescente, adulto ou idoso.


def classificar_idade(idade):
    if idade < 0:
        return "Idade inválida"
    elif idade < 12:
        return "Criança"
    elif idade < 18:
        return "Adolescente"
    elif idade < 60:
        return "Adulto"
    else:
        return "Idoso"

try:
    idade_usuario = int(input("Digite sua idade: "))
 
    classificacao = classificar_idade(idade_usuario)
    print(f"Você é classificado como {classificacao}.")
except ValueError:
    print("Por favor, digite um valor numérico para a idade.")