
# Crie uma função chamada contar_vogais que recebe uma string como parâmetro. Implemente a lógica para contar o número de vagais na string
# e retorne o total de vogais. Solicite ao usuário para inserir uma frase e utilize a função para contar as vogais.


# OBS Este programa solicitará ao usuário que insira uma frase, contará o número de vogais usando a função contar_vogais e imprimirá o resultado. 
# Note que a função considera tanto vogais maiúsculas quanto minúsculas, pois converte cada caractere para minúsculo antes de verificar se é uma vogal.

def contar_vogais(frase):
    # Inicializa o contador de vogais
    total_vogais = 0

    # Itera sobre cada caractere na string
    for char in frase:
        # Verifica se o caractere é uma vogal
        if char.lower() in "aeiou":
            total_vogais += 1

    # Retorna o total de vogais encontradas na string
    return total_vogais

# Solicita ao usuário para inserir uma frase
frase_usuario = input("Digite uma frase: ")

# Chama a função e exibe o resultado
resultado = contar_vogais(frase_usuario)
print(f"Total de vogais na frase: {resultado}")




# OBS
# def contar_vogais(frase):: Define a função contar_vogais que recebe uma string chamada frase como parâmetro.

# total_vogais = 0: Inicializa uma variável chamada total_vogais com o valor zero. Esta variável será usada para contar o número de vogais na string.

# for char in frase:: Inicia um loop for que itera sobre cada caractere (char) na string frase.

# if char.lower() in "aeiou":: Verifica se o caractere convertido para minúsculo (char.lower()) está presente na string "aeiou", que representa as vogais em minúsculas.

# total_vogais += 1: Se o caractere for uma vogal, incrementa o contador total_vogais em 1.

# return total_vogais: Retorna o total de vogais encontradas na string após percorrer todos os caracteres.

# frase_usuario = input("Digite uma frase: "): Solicita ao usuário que digite uma frase e armazena a entrada na variável frase_usuario.

# resultado = contar_vogais(frase_usuario): Chama a função contar_vogais passando a frase inserida pelo usuário como argumento e armazena o resultado na variável resultado.

# print(f"Total de vogais na frase: {resultado}"): Imprime na tela o resultado, indicando o total de vogais na frase inserida pelo usuário. A f-string é usada para formatar a mensagem.