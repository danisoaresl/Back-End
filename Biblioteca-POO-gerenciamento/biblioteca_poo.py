from datetime import datetime
import sqlite3
import uuid


class Usuario:
    def __init__(self, nome, telefone, nacionalidade):
        self.id = str(uuid.uuid4())
        self.nome = nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade


class Livro:
    def __init__(self, titulo, editora, generos, max_renovacoes):
        self.titulo = titulo
        self.editora = editora
        self.generos = generos
        self.max_renovacoes = max_renovacoes
        self.exemplares_disponiveis = []
        self.exemplares_emprestados = []

    def adicionar_exemplar(self, quantidade):
        for _ in range(quantidade):
            exemplar = Exemplar(self)
            self.exemplares_disponiveis.append(exemplar)

    def calcular_qtd_disponiveis(self):
        return len(self.exemplares_disponiveis)

    def calcular_qtd_emprestados(self):
        return len(self.exemplares_emprestados)

    def calcular_qtd_devolvidos(self):
        return len([exemplar for exemplar in self.exemplares_emprestados if exemplar.status == "Devolvido"])

    def emprestar_exemplar(self):
        if self.exemplares_disponiveis:
            exemplar_emprestimo = self.exemplares_disponiveis.pop(0)
            exemplar_emprestimo.emprestar()
            self.exemplares_emprestados.append(exemplar_emprestimo)
            return exemplar_emprestimo
        else:
            return None

    def devolver_exemplar(self, exemplar):
        if exemplar in self.exemplares_emprestados:
            exemplar.devolver()
            self.exemplares_emprestados.remove(exemplar)
            self.exemplares_disponiveis.append(exemplar)


class Exemplar:
    def __init__(self, livro):
        self.id = str(uuid.uuid4())
        self.livro = livro
        self.status = "Disponivel"

    def emprestar(self):
        if self.status == "Disponivel":
            self.status = "Emprestado"
            return True
        else:
            return False

    def devolver(self):
        self.status = "Disponivel"


class Emprestimo:
    def __init__(self, exemplar, usuario):
        self.id = str(uuid.uuid4())
        self.exemplar = exemplar
        self.usuario = usuario
        self.data_emprestimo = datetime.now()
        self.data_devolucao = None

    def emprestar(self):
        if self.exemplar.emprestar():
            self.data_emprestimo = datetime.now()
            return True
        else:
            return False

    def devolver(self):
        if self.exemplar.status == "Emprestado":
            self.exemplar.devolver()
            self.data_devolucao = datetime.now()
            return True
        else:
            return False

    def __str__(self):
        return f"Empréstimo - ID: {self.id}, Livro: {self.exemplar.livro.titulo}, " \
               f"ID do Exemplar: {self.exemplar.id}, " \
               f"Usuário: {self.usuario.nome}, " \
               f"Data de Empréstimo: {self.data_emprestimo}, Data de Devolução: {self.data_devolucao}"


class Biblioteca:
    def __init__(self):
        self.livros = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)

    def cadastrar_usuario(self, usuario):
        conexao = sqlite3.connect('biblioteca_poo.db')
        conexao.execute("INSERT INTO Usuario (id, nome, telefone, nacionalidade) VALUES (?,?,?,?)",
                        (usuario.id, usuario.nome, usuario.telefone, usuario.nacionalidade))
        conexao.commit()
        conexao.close()

    def realizar_emprestimo(self, livro, usuario):
        exemplar_emprestimo = livro.emprestar_exemplar()
        if exemplar_emprestimo:
            emprestimo = Emprestimo(exemplar_emprestimo, usuario)
            return emprestimo
        else:
            return None

    def realizar_devolucao(self, emprestimo):
        emprestimo.exemplar.livro.devolver_exemplar(emprestimo.exemplar)
        emprestimo.data_devolucao = datetime.now()

    def exibir_estado_exemplares(self):
        for livro in self.livros:
            print(f"\nLivro: {livro.titulo}")
            print(f"Quantidade disponível: {livro.calcular_qtd_disponiveis()}")
            print(f"Quantidade emprestada: {livro.calcular_qtd_emprestados()}")
        


# Exemplo de uso
biblioteca = Biblioteca()

# Criar usuários
usuario1 = Usuario("João", "123456789", "Brasileiro")
usuario2 = Usuario("Maria", "987654321", "Português")

# Criar livros
livro1 = Livro("O Poder do Hábito", "Editora XYZ", ["Autoajuda"], 2)
livro2 = Livro("O Milagre da Manhã", "Editora ABC", ["Autoajuda"], 3)

# Adicionar exemplares aos livros
livro1.adicionar_exemplar(5)
livro2.adicionar_exemplar(5)

# Cadastrar livros na biblioteca
biblioteca.cadastrar_livro(livro1)
biblioteca.cadastrar_livro(livro2)

# Cadastrar usuários na biblioteca
biblioteca.cadastrar_usuario(usuario1)
biblioteca.cadastrar_usuario(usuario2)

# Exibir estado dos exemplares antes dos empréstimos
biblioteca.exibir_estado_exemplares()

# Realizar empréstimo de 3 exemplares
for _ in range(3):
    emprestimo = biblioteca.realizar_emprestimo(livro2, usuario1)
    if emprestimo:
        print(emprestimo)
    else:
        print("Não foi possível realizar o empréstimo. Estoque zerado.")
        
for _ in range(2):
    emprestimo = biblioteca.realizar_emprestimo(livro1, usuario1)
    if emprestimo:
        print(emprestimo)
    else:
        print("Não foi possível realizar o empréstimo. Estoque zerado.")

# Exibir estado dos exemplares após os empréstimos
biblioteca.exibir_estado_exemplares()

