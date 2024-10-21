
# Crie um dicionário representando contatos (nome, telefone). Permita ao usuário procurar por um contato pelo nome.



contatos = {
    'Guto': '222-321-6102',
    'Inez': '168-333-8691',
    'Enzo': '444-315-5102',
    'Samuel':'555-287-3202'
}


def procurar_contato(nome):
    if nome in contatos:
        return f"Nome: {nome}, Telefone: {contatos[nome]}"
    else:
        return f"Contato com o nome '{nome}' não encontrado."


nome_procurado = input("Digite o nome do contato que deseja procurar: ")


resultado_procura = procurar_contato(nome_procurado)
print(resultado_procura)


