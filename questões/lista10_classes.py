#1 – Crie uma classe que modele uma bola:
#Atributos: cor, circunferencia, material
#Métodos: set_cor (string) e get_cor()
class Bola:
  def __init__(self, cor, circunferencia, material):
      self.cor = cor
      self.circunferencia = circunferencia
      self.material = material

  def set_cor(self, nova_cor):
      self.cor = nova_cor

  def get_cor(self):
      return self.cor

cor = input("Digite a cor: ")
circunferencia = float(input("Digite a circunferencia: "))
material = input("Digite o material: ")

bola1 = Bola(cor, circunferencia, material)

nova_cor = input("Digite a nova cor: ")
bola1.set_cor(nova_cor)

print("Cor:", bola1.get_cor())
print("Circunferência:", bola1.circunferencia)
print("Material:", bola1.material)

#2– Classe Quadrado: Crie uma classe que modele um quadrado:
#Atributos: lado
#Métodos: set_lado (float), get_lado(), calcula_area()
class Quadrado:
  def __init__(self,lado):
     self.lado = lado
    
  def set_lado(self, novo_lado):
      self.lado = novo_lado
      
  def get_lado(self):
      return self.lado
      
  def calcula_area(self):
      area = self.lado**2
      return area

lado = float(input("Digite o lado do quadrado: "))

quadrado1 = Quadrado(lado)
print("A área é {:.1f}".format(quadrado1.calcula_area()))

#3 – Classe Retângulo: Crie uma classe que modele um retângulo:
#Atributos: comprimento, largura
#Métodos: get_comprimento(), get_largura(), set_comprimento (float), set_largura (float), calcula_area()
class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def set_comprimento(self,comprimento):
        self.comprimento = comprimento
    def get_comprimento(self):
        return self.comprimento

    def set_largura(self,largura):
        self.largura = largura
    def get_largura(self):
        return self.largura

    def calcula_area(self):
        return self.comprimento * self.largura

largura = float(input("Digite a largura: "))
comprimento = float(input("Digite o comprimento: "))

retangulo1 = Retangulo(comprimento,largura)
print("A área é {:.1f}".format(retangulo1.calcula_area()))

#4 – Crie uma classe que modele um calculadora:
#Atributos : — nenhum —
#Métodos: somar (float, float), subtrair (float, float), multiplicar (float, float), dividir (float, float)
class Calculadora:
    def soma(self,a,b):
        return a + b
    def subtração(self,a,b):
        return a - b
    def multiplicação(self,a,b):
        return a * b
    def divisão(self,a,b):
        return a / b
        
a = float(input("A = "))
b = float(input("B = "))

calculadora1 = Calculadora()
soma = calculadora1.soma(a, b)
sub = calculadora1.subtração(a, b)
multi = calculadora1.multiplicação(a, b)
divi = calculadora1.divisão(a, b)

print("Soma =", soma)
print("Subtração =", sub)
print("Multiplicação =", multi)
print("Divisão =", divi)

#5 – Classe Macaco: Desenvolva uma classe Macaco, que possua os atributos nome e barriga, e pelo menos os métodos comer (string), ver_barriga() e digerir(). Em seguida, teste sua classe criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estômago a cada refeição.
class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.barriga = []

    def comer(self, comida):
        self.barriga.append(comida)

    def ver_barriga(self):
        return self.barriga

    def digerir_comida(self, comida):
        if comida in self.barriga:
            self.barriga.remove(comida)
        else:
            print("Essa comida não está na barriga do macaco.")

nome = input("Digite o nome do macaco: ")

macaco1 = Macaco(nome)
comida = input("Digite a comida para o macaco 1: ")
macaco1.comer(comida)
print("Barriga do macaco 1:", macaco1.ver_barriga())

macaco2 = Macaco(nome)
comida = input("Digite a comida para o macaco 2: ")
macaco2.comer(comida)
print("Barriga do macaco 2:", macaco2.ver_barriga())
macaco2.digerir_comida(comida)
print("Barriga do macaco 2 após a digestão:", macaco2.ver_barriga())
comida = input("Digite outra comida para o macaco 2: ")
macaco2.comer(comida)
print("Barriga do macaco 2 após comer novamente:", macaco2.ver_barriga())

#6 - Classe Conta: Crie uma classe que modele uma conta bancária e depois execute as operações abaixo:
#Atributos: numero, titular, saldo, data_criacao
#Métodos: creditar (float), debitar (int), get_numero, get_titular, get_saldo, get_data_criacao
#Deve ser criado um construtor, que seta o número da conta para o valor passado como parâmetro, o titular para o valor passado como parâmetro, o saldo para 0 e a data para o dia de hoje.
class Conta:
    def __init__(self,numero,titular,saldo,data_criacao):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.data_criacao = data_criacao

    def get_numero(self):
        return self.numero

    def get_titular(self):
        return self.titular

    def get_saldo(self):
        return self.saldo

    def get_data_criacao(self):
        return self.data_criacao

    def creditar(self,valor):
        self.saldo += valor

    def debitar(self,valor):
        self.saldo -= valor

numero = int(input("Digite o número da conta: "))
titular = input("Digite o nome do titular da conta: ")
saldo = float(input("Digite o saldo da conta: "))
data_criacao = input("Digite a data de criação da conta: ")

conta1 = Conta(numero,titular,saldo,data_criacao)
print("Número da conta:", conta1.get_numero())
print("Titular da conta:", conta1.get_titular())
print("Saldo da conta:", conta1.get_saldo())
print("Data de criação da conta:", conta1.get_data_criacao())
valor = float(input("Digite o valor a ser creditado na conta: "))
conta1.creditar(valor)
print("Saldo da conta após o crédito:", conta1.get_saldo())
valor = float(input("Digite o valor a ser debitado da conta: "))

