# Peça ao usuário para informar o ano de nascimento. Em seguida, calcule e imprima a idade atual.


from datetime import date

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

try:
    birth_year = int(input("Digite o ano de nascimento (YYYY): "))
    birthDate = date(birth_year, int(input("Digite o mês de nascimento (MM): ")), int(input("Digite o dia de nascimento (DD): ")))

  
    print("Idade:", calculateAge(birthDate), "anos")

except ValueError:
    print("Entrada inválida. Certifique-se de fornecer valores numéricos para o ano, mês e dia.")

