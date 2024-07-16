#1. Crie um programa que lê um número. Se o número for maior do que 100, então imprima metade do número.
numero = float(input("Digite o número: "))
if numero > 100:
    metade = numero / 2
    print("A sua metade é",metade)
else:
    print(numero)
    
#2. Crie um programa que lê dois números. Em seguida, faça a soma dos dois números. Se o resultado for maior ou igual a 100, o programa deve imprimir o resultado. Independente do resultado, o programa também deve anunciar que chegou ao fim do código.  
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o valor do segundo número: "))

soma = n1 + n2

if soma >= 100:
    print("Soma:",soma)
    print("FIM! :D")
else:
    print("FIM! :D")    

#3. Crie um programa que recebe dois números e imprime o maior deles.
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))

if n1 > n2:
    print("Número 1 é maior! ")
    
elif n2 > n1:
    print("Número 2 é maior! ")

else:
    print("Os dois são iguais! ")  

#4. Crie um programa que lê um número e diz se ele é maior do que 0, menor do que 0 ou é 0.
numero = float(input("Digite o número: "))
if numero > 0:
    print("Esse número é maior do que zero! ")
elif numero < 0:
    print("Esse número é menor do que zero! ")
else:
    print("Esse número é zero! ")

#5. Crie um programa que pergunta a idade do usuário. Se a resposta for menor do que 18, imprima “você é menor de idade”, se tiver entre 18 e 65, imprima “você é adulto”, se for acima de 65 anos, imprima “você é idoso”. 
idade = int(input("Digite a sua idade: "))
if idade < 18:
    print("Você é menor de idade! ")
elif idade >= 18 and idade < 65:
    print("Você é adulto! ")
else:
    print("Você é idoso! ") 

#6. Escreva um código que lê um número e diz se o número é par ou ímpar. 
numero = float(input("Digite o número: "))
if numero % 2 == 0:
    print("Esse número é par !")
else:
    print("Esse número é ímpar !")

#7. Crie um programa que irá funcionar como uma calculadora. Primeiro, o programa deve receber dois números, e em seguida um símbolo que representa uma operação matemática (+ para soma, - para subtração, * para multiplicação e / para divisão). Por fim, imprima o resultado da conta.      
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

opcao = input("Qual opção deseja? (+ - soma, - - subtração, * - multiplicação e / - divisão): ")
if opcao == "+":
    soma = n1 + n2
    print("A soma é:",soma)
elif opcao == "-":
    subtração = n1 - n2
    print("A subtração é:",subtração)
elif opcao == "*":
    multiplicação = n1*n2
    print("A multiplicação é",multiplicação)
else:
    divisão = n1 / n2
    print("A divisão é",divisão)
    
#8. Escreva um código que recebe um número. Caso o número seja positivo, imprima a raiz quadrada. Caso seja negativo, imprima o quadrado do número.
import math
numero = float(input("Número: "))
if numero >= 0:
    raiz_quadrada = math.sqrt(numero)
    print(raiz_quadrada)
else:
    quadrado = numero**2
    print(quadrado) 

#9. Faça um programa que recebe duas notas de um aluno. O programa deve calcular a média e dar o seguinte resultado: Se a média for maior ou igual a 7,0, imprima “Aprovado”. Se a média for menor que 4,0, imprima “Reprovado”. Se a média for 10,0, imprima “Aprovadíssimo”.Se a média for menor que 7,0 mas maior ou igual a 4,0, imprima “Final”, e em seguida receba mais uma nota. Se a nota da final for maior ou igual a 5,0, imprima “Aprovado na final”. Se a nota da final for menor que 5,0, imprima “Reprovado na final”.
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: ")) 
media = (nota1+nota2)/2
if media >=7 and media <10:
    print("Aprovado! ")
elif media < 4:
    print("Reprovado!")
elif media == 10:
    print("Aprovadissímo! ")
elif media <7 and media >=4:
    print("Final!") 
    nota = float(input("Nota da final: "))
    if nota >=5:
        print("Aprovado na final!")
    else:
        print("Reprovado na final!")                                 
    
                                   