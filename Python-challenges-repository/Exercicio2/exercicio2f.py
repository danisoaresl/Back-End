
# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

# OBS este exemplo, a função reverso_numero recebe um número inteiro, converte-o para string, inverte a string usando a notação de 
# fatiamento ([::-1]) e, em seguida, converte a string invertida de volta para um número inteiro. O programa solicita ao usuário que 
# insira um número, chama a função com esse número e imprime o reverso.

def reverso_numero(numero):
    # Convertendo o número para string para facilitar a inversão
    numero_str = str(numero)
    
    # Invertendo a string
    numero_invertido_str = numero_str[::-1]
    
    # Convertendo a string invertida de volta para um número inteiro
    numero_invertido = int(numero_invertido_str)
    
    return numero_invertido

# Exemplo de uso da função
numero_original = int(input("Digite um número inteiro: "))

numero_invertido = reverso_numero(numero_original)

print(f"O reverso do número {numero_original} é: {numero_invertido}")



