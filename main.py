from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica

p1 = Pessoa(1, 'Pessoa1', 'Rua Leal', '89551262')
p1.imprimirNome()
p1.getTelefone()
p2 = Fisica('0315775556', '27', 65, 1.67)
p2.imprimirCPF()
p2.GetIMC()
p3 = Juridica('66562625626', 'Empresa1','40')
p3.imprimirCNPJ()
p3.GetNotaFiscal()
