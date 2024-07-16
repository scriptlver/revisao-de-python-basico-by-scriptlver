#1. Crie um programa que escreva “Olá, Mundo!” na tela
print("Olá, Mundo!")

#2. Realize a leitura de 2 floats e imprima as seguintes operações: soma, subtração, multiplicação, divisão e resto da divisão.
float1 = float(input("Digite o valor do primeiro número: ")) #input: o próprio usuário digitar suas respostas
float2 = float(input("Digite o valor do segundo número: "))

#soma
soma = float1 + float2

#subtração
sub = float1 - float2

#multiplicação
mult = float1 * float2

#divisão
div = float1 / float2

#resto
resto = float1 % float2

print("Soma:",soma)
print("Subtração:",sub)
print("Multiplicação:",mult)
print("Divisão:",div)
print("Resto de divisão:",resto)

#3. Realize a leitura de 1 inteiro e imprima o seu antecessor e o seu sucessor.
int = int(input("Digite o valor do int: "))
ant = int - 1
suc = int + 1

print("Antecessor:",ant)
print("Sucessor:",suc)

#4. Realize a leitura de 1 inteiro e imprima o dobro, triplo e metade do valor lido.
int = int(input("Digite o valor do int: "))

#dobro
dobro = int*2

#triplo
triplo = int*3

#metade
metade = int/2

print("Dobro:",dobro)
print("Triplo:",triplo)
print("Metade:",metade)

#5. Realize a leitura de 3 floats e imprima a média aritmética.
float1 = float(input("Digite o valor do primeiro float: "))
float2 = float(input("Digite o valor do segundo float: "))
float3 = float(input("Digite o valor do terceiro float: "))

media = (float1+float2+float3) / 3
print("A média é: %.1f" % media)

#6. Realize a leitura de 1 float referente ao valor de um produto e imprime o valor com descontos de 10%, 20% e 50%.
valor = float(input("Valor: " ))
desconto_10 = valor * 0.9
desconto_20 = valor * 0.8
desconto_50 = valor * 0.5

print("Com desconto de 10%:",desconto_10)
print("Com desconto de 20%:",desconto_20)
print("Com desconto de 50%:",desconto_50)

# 7. Realize a leitura de 1 float referente ao salário do cidadão e apresenta o salário com reajuste de 10% da inflação.
float = float(input("Digite o valor do float: "))
reajuste = float * 1.1
print("O valor com o reajuste é %.1f" % reajuste)

#8. Crie um programa que leia dois valores: o primeiro é o tamanho da base de um triângulo, e o segundo é a altura. Calcule e imprima a área do triângulo.
base = float(input("Base: "))
altura = float(input("Altura: "))
area = base*altura/2
print("A área é:",area)

#9. Crie um programa que calcula a soma dos quadrados de três números digitados pelo usuário.
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))

q1 = n1**2
q2 = n2**2
q3 = n3**2

soma = q1 + q2 + q3

print("A soma do quadrado dos três números é",soma)

#10. Crie um programa que recebe um valor de peso em quilos e o converte para libras.
valor = float(input("Digite o valor em kg: "))
conversão = valor * 2.2
print("O valor em libras é",conversão)

#11. Crie um programa que recebe um valor de temperatura em Celsius e o converte para Kelvin e Fahrenheit.
temp_c = float(input("Digite a temperatura em Celsius: "))
c_k = temp_c + 273.5
c_f = 1.8 * temp_c + 32

print("Celsius para Kelvin:",c_k)
print("Celsius para Fahrenheit:",c_f)

