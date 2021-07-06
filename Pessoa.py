
class Pessoa():
    def __init__(self, id, nome, endereco, telefone):
        self.__id = id
        self.nome = nome
        self._endereco = endereco
        self.__telefone = telefone

    def imprimirNome(self):
        print(f"Nome: {self.nome}")

    def __imprimirTelefone(self):
        print(f"Telefone: {self.__telefone}")

    def getTelefone(self):
        self.__imprimirTelefone()