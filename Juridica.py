from Pessoa import Pessoa

class Juridica():
    def __init__(self, cnpj, inscricaoEstatudal, qtdFuncionarios):
        self.__cnpj = cnpj
        self.__inscricaoEstatudal = inscricaoEstatudal
        self.qtdFuncionarios = qtdFuncionarios

    def imprimirCNPJ(self):
        print("CNPJ ", self.__cnpj)


    def __emitirNotaFiscal(self):
        print('Emissao nota fiscal')

    def GetNotaFiscal(self):
        self.__emitirNotaFiscal()