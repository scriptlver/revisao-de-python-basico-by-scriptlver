#1 – Crie um programa que escreva os números de 1 a 15 usando for
for i in range(1,16):
    print(i)
    
#2 – Crie um programa que lê um número inteiro positivo e escreve os números de 1 até o número digitado. 
numero = int(input("Digite um número inteiro positivo: "))
for i in range(1,numero+1):
    print(i)
    
#3 – Crie um programa que faz a soma de todos os números entre 1 e 100 usando for.   
soma = 0
for num in range(1,101):
    soma = num + soma
print(soma)

#4 – Crie um programa que lê um número inteiro positivo e faz as somas de todos os números entre 1 e o número digitado.
numero = int(input("Digite um número inteiro positivo: "))
soma = 0
for num in range(1,numero+1):
    soma = num + soma  
print(soma) 

#5 – Crie um programa que lê um número inteiro positivo e imprime a “tabuada” desse número. Use for.
numero = int(input("Digite um número inteiro positivo: "))
print("Tabuada do",numero,":")
for i in range(1,11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    
#6 – Crie um algoritmo que entre com cinco números e imprima o quadrado de cada número.
numero_1 = int(input("Digite um número inteiro positivo: "))
numero_2 = int(input("Digite um número inteiro positivo: "))
numero_3 = int(input("Digite um número inteiro positivo: "))
numero_4 = int(input("Digite um número inteiro positivo: "))
numero_5 = int(input("Digite um número inteiro positivo: "))

print(numero_1**2)
print(numero_2**2)
print(numero_3**2)
print(numero_4**2)
print(numero_5**2)

#7 – Crie um algoritmo que imprima todos os números pares de 1 a 10.
for i in range(1,10):
    if i % 2 == 0:
        print(i)
    
#8 – Crie um algoritmo que leia um número que será o limite superior de um intervalo e imprimatodos os números ímpares menores do que esse número. Exemplo: Limite superior: 15 Saída: 1 3 5 7 9 11 13
numero = int(input("Digite um número limite: "))
for num in range(1,numero):
    if num % 2 != 0:
        print(num)
        
#9 – Crie um programa que imprima todos os números entre 1 e 20 em ordem decrescente usando for.
for i in range(20,0,-1):
    print(i)
    
#10 – Crie um programa que imprime uma lista de números, começando com um valor X, indo até um valor Y (incluído), fazendo incrementos de Z por vez. X, Y e Z devem ser números inteiros digitados pelo usuário.        
start = int(input("Digite o número inicial: "))
step = int(input("Digite o número de incrementos: "))
stop = int(input("Digite o número final: "))
for i in range(start,stop+1,step):
    print(i)
  