from Pessoa import Pessoa

class Fisica():
    def __init__(self, cpf, idade, peso, altura):
        self.__cpf = cpf
        self.idade = idade
        self.peso = float(peso)
        self.altura = float(altura)

    def imprimirCPF(self):
        print("CPF: ", self.__cpf)

    def __calculaIMC(self):
        altura_quadrado = self.altura * self.altura
        imc = self.peso/ altura_quadrado
        print('IMC: ', imc)

    def GetIMC(self):
        self.__calculaIMC()