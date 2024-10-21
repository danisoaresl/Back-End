
# Crie um dicionário representando um carrinho de compras. Adicione produtos (chaves) e quantidades (valores) ao carrinho. Calcule o total do carrinho de compra.



carrinho_compras = {
     'iogurte': 6,
     'leite': 2,
     'castanhas': 1,
     'arroz': 1,
    'bananas': 12
}

precos = {
     'iogurte': 10.0,
     'leite': 6.50,
     'castanhas': 18.0,
     'arroz': 30.0,
     'bananas': 15.0
}



total = 0.0
for produto, quantidade in carrinho_compras.items():
    if produto in precos:
        total += precos[produto] * quantidade
    else:
        print(f"O produto '{produto}' não possui um preço definido.")

print(f"Total do carrinho de compras: R${total:.2f}")
