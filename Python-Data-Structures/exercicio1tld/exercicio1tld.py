
# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
# As perguntas são:
# ""Telefonou para a vítima?""
# ""Esteve no local do crime?""
# ""Mora perto da vítima?""
# ""Já trabalhou com a vítima?""

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice""" e 5 como ""Assassino"".
# Caso contrário, ele será classificado como ""Inocente""".


respostas = []

def fazer_pergunta(pergunta):
    resposta = input(pergunta + " (sim/não): ").lower()
    return resposta == "sim"

respostas.append(fazer_pergunta("Telefonou para a vítima?"))
respostas.append(fazer_pergunta("Esteve no local do crime?"))
respostas.append(fazer_pergunta("Mora perto da vítima?"))
respostas.append(fazer_pergunta("Já trabalhou com a vítima?"))

num_respostas_positivas = respostas.count(True)

if num_respostas_positivas == 5:
    print("Assassino")
elif 3 <= num_respostas_positivas <= 4:
    print("Cúmplice")
elif num_respostas_positivas == 2:
    print("Suspeita")
else:
    print("Inocente")