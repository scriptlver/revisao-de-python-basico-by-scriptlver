#1 – Crie um método “potencia” que receba dois números a e b (base e expoente, respectivamente) e retorne a elevado a b .
def calcular_potencia(base_a,expoente_b):
    potencia = base_a**expoente_b
    print(potencia)
base_a = float(input("Digite o valor da base: "))
expoente_b = float(input("Digite o valor do expoente: "))
calcular_potencia(base_a,expoente_b)

#2 – Crie um método que permita a conversão de graus Celsius para Fahrenheit. Fórmula: 9/5.0*C+32. A função deve retornar a temperatura convertida.
def conversão(temp_celsius):
    conver_temp = (9/5*temp_celsius)+32
    print(conver_temp)
temp_celsius = float(input("Digite o valor da temperatura em celsius: "))
conversão(temp_celsius)

#3 – Crie um método “numero_par” que permita verificar se um dado número x, passado como parâmetro é um número par. A função deve retornar “True” ou “False”    
def numero_par(numero_x):
    print("Descubra se um número é par!")   
    numero_x = int(input("Digite um número: "))
    if numero_x % 2 == 0:
        print("True")
    else:
        print("False")
numero_par(0)

#4 – Faça uma função que retorne a quantidade de dígitos de um determinado número inteiro informado.
def contar_digitos(numero):
    numero_string = str(numero)
    quantidade_digitos = len(numero_string)
    print("O número tem",quantidade_digitos,"digitos")
numero = int(input("Digite um número: "))
contar_digitos(numero)

#5 – Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
def reverso_numero(numero):
    reverso_str = str(numero)
    reverso = reverso_str[::-1]
    reverso_int = int(reverso)
    print("O reverso do número é",reverso_int)
numero = int(input("Digite um número: "))
reverso_numero(numero) 

#6 – Faça uma função que calcule o fatorial de um número passado como parâmetro. A função deve retornar o resultado.
def calcular_fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado
numero = int(input("Digite o número: "))
resultado = calcular_fatorial(numero)
print("O fatorial do número é", resultado)

 
    

      
                
      