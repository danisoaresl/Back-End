
# Implemente um programa que classifique um aluno com base em sua pontuação em um exame.
# O programa deverá solicitar uma nota de 0 a 10. Se a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é reprovado.


while True:
    try:
        nota = float(input("Digite a nota do aluno (entre 0 e 10): "))
        
        if 0 <= nota <= 10:
            if nota >= 7:
                print("Aluno aprovado!")
            else:
                print("Aluno reprovado.")
            break
        else:
            print("Valor inválido. A nota deve estar entre 0 e 10.")
    except ValueError:
        print("Por favor, digite um valor numérico.")
