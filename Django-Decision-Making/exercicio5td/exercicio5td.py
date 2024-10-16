
# Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
# equilátero: todos os lados com o mesmo valor
# isósceles: dois lados com o mesmo valor
# escaleno: todos os lados com medidas distintas.


def classificar_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

def main():
    print("Digite os comprimentos dos três lados do triângulo:")
    lado_a = float(input("Lado A: "))
    lado_b = float(input("Lado B: "))
    lado_c = float(input("Lado C: "))

    if lado_a <= 0 or lado_b <= 0 or lado_c <= 0:
        print("Por favor, insira valores positivos para os lados do triângulo.")
    else:
        tipo_triangulo = classificar_triangulo(lado_a, lado_b, lado_c)
        print(f"O triângulo é do tipo: {tipo_triangulo}")

if __name__ == "__main__":
    main()