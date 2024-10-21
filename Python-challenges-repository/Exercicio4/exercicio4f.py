
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de
# cada moeda estrangeira. Considere a tabela de conversão abaixo:

# Dólar Americano: R$ 4,91
# Peso Argentino: R$ 0,02
# Dólar Australiano: R$ 3,18
# Dólar Canadense: R$ 3,64
# Franco Suiço: R$ 0,42
# Euro: R$ 5,36
# Libra esterlina: R$ 6,21

# OBS Este programa solicita ao usuário que digite o valor em reais na carteira e, em seguida, calcula e 
# exibe quanto dinheiro ele poderia comprar em cada moeda estrangeira com base nas taxas de conversão fornecidas.




def converter_moeda_estrangeira(valor_em_reais, taxa_de_conversao):
    valor_convertido = valor_em_reais / taxa_de_conversao
    return valor_convertido

def main():
    # Definindo as taxas de conversão
    taxa_dolar_americano = 4.91
    taxa_peso_argentino = 0.02
    taxa_dolar_australiano = 3.18
    taxa_dolar_canadense = 3.64
    taxa_franco_suico = 0.42
    taxa_euro = 5.36
    taxa_libra_esterlina = 6.21

    # Obtendo o valor em reais da carteira da pessoa
    valor_em_reais = float(input("Digite o valor em reais na sua carteira: R$ "))

    # Convertendo para cada moeda estrangeira
    valor_dolar_americano = converter_moeda_estrangeira(valor_em_reais, taxa_dolar_americano)
    valor_peso_argentino = converter_moeda_estrangeira(valor_em_reais, taxa_peso_argentino)
    valor_dolar_australiano = converter_moeda_estrangeira(valor_em_reais, taxa_dolar_australiano)
    valor_dolar_canadense = converter_moeda_estrangeira(valor_em_reais, taxa_dolar_canadense)
    valor_franco_suico = converter_moeda_estrangeira(valor_em_reais, taxa_franco_suico)
    valor_euro = converter_moeda_estrangeira(valor_em_reais, taxa_euro)
    valor_libra_esterlina = converter_moeda_estrangeira(valor_em_reais, taxa_libra_esterlina)

    # Exibindo os resultados
    print(f"Com R$ {valor_em_reais:.2f} você poderia comprar:")
    print(f"Dólar Americano: ${valor_dolar_americano:.2f}")
    print(f"Peso Argentino: ${valor_peso_argentino:.2f}")
    print(f"Dólar Australiano: ${valor_dolar_australiano:.2f}")
    print(f"Dólar Canadense: ${valor_dolar_canadense:.2f}")
    print(f"Franco Suiço: CHF {valor_franco_suico:.2f}")
    print(f"Euro: € {valor_euro:.2f}")
    print(f"Libra Esterlina: £ {valor_libra_esterlina:.2f}")

if __name__ == "__main__":
    main()