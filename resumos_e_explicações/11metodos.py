#11. MÉTODOS: funções de algo
#sem input
def calcular_imc(altura,peso): #método criado para realizar o calculo do imc
    imc = peso/altura**2
    return imc
retorno = calcular_imc(1.67,57.1)
print(retorno)

#com input
def calcular_imc(altura,peso):
    imc = peso / altura**2
    print(imc)
altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso em kg: "))    
calcular_imc(altura,peso)

def somar_numeros(n1,n2):
    soma = n1 + n2
    return soma
retorno = somar_numeros(10,5)
print(retorno)

def area_triangulo(base,altura):
    area = (base*altura) / 2
    print(area)
base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))  
area_triangulo(base,altura)  

#usado para criar funções para uma classe
#parâmetros = o que vai precisar para realizar a função, exemplo: somar números (parâmetros = base e altura)

    
    