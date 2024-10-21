
# Faça um programa que peça as quatro notas de 5 alunos, calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.



medias_alunos = []

for i in range(5):

    nota1 = float(input(f"Informe a nota 1 do aluno {i + 1}: "))
    nota2 = float(input(f"Informe a nota 2 do aluno {i + 1}: "))
    nota3 = float(input(f"Informe a nota 3 do aluno {i + 1}: "))
    nota4 = float(input(f"Informe a nota 4 do aluno {i + 1}: "))

    media = (nota1 + nota2 + nota3 + nota4) / 4
 
    medias_alunos.append(media)

alunos_aprovados = sum(1 for media in medias_alunos if media >= 7.0)

print(f"\nNúmero de alunos com média maior ou igual a 7.0: {alunos_aprovados}")