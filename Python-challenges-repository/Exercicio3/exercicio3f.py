
# Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou 
# vice-versa. Para cada opção, crie uma função.

# Plus: Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de 
# conversão correta.2


# OBS cript em Python que realiza a conversão de temperatura de Celsius para Fahrenheit e vice-versa, com um menu para 
# o usuário escolher a opção desejada:


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter_menu():
    print("Escolha uma opção:")
    print("1. Converter de Celsius para Fahrenheit")
    print("2. Converter de Fahrenheit para Celsius")

    choice = input("Digite o número da opção desejada (1 ou 2): ")

    if choice == "1":
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        result = celsius_to_fahrenheit(celsius)
        print(f"{celsius} graus Celsius é igual a {result} graus Fahrenheit.")
    elif choice == "2":
        fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
        result = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} graus Fahrenheit é igual a {result} graus Celsius.")
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    temperature_converter_menu()
