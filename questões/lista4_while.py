#1 – Faça um programa que lê números enquanto forem positivos (digitados pelo usuário) e imprime quantos números foram digitados.
contador = 0
while True:
    numero = int(input("Digite um número positivo (ou negativo para sair): "))
    if numero >= 0:
        contador += 1
    else:
        break  
print("Você digitou", contador, "números positivos.")

#2 – Crie um algoritmo que leia vários números inteiros e apresente o quadrado de cada número. O algoritmo se encerra quando se digita o número 0.
quadrado = 0
while True:
    numero = int(input("Digite um número inteiro (ou 0 para encerrar): "))
    if numero > 0:
        quadrado = numero**2
        print("O quadrado de",numero,"é",quadrado)    
    else:
        break

#3 – Escreva um laço que calcule
#a. A soma de todos os números pares entre 2 e 100 (inclusive).
#b. A soma de todos os números ímpares entre 1 e 100.
#c. A soma de todos os quadrados dos números entre 1 e 100 (inclusive). 

soma_pares = 0
soma_impares = 0
soma_quadrados = 0
cont = 0
while True:
  cont = cont + 1
  if cont > 100:
    break
  soma_quadrados = soma_quadrados + cont**2
  if cont % 2 == 0:
    soma_pares = soma_pares + cont
  elif cont % 2 != 0:
    soma_impares = soma_impares + cont
  
print("a) %d" % soma_pares)
print("b) %d" % soma_impares)
print("c) %d" % soma_quadrados)

#4 – Reescreva o seguinte laço for com um laço while.
s = 0
i = 1 
while i <= 9:
    s += i
    i += 1  
print("A soma dos números de 1 a 9 é:", s)

#5 – Faça um programa que peça para N pessoas a sua idade, ao final o programa deverá verificar se a média de idade da turma está entre 0 e 25, 26 e 60 ou é maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
contador_n = 0
soma_idades = 0
while True:
    idade = int(input("Digite a sua idade (ou -1 para sair.) "))
    if idade >= 0:
        soma_idades+=idade
        contador_n+=1
    else:
        break
media = soma_idades/contador_n
if media >= 0 and media <=25:
    print(f"A média da idade da turma é {media:.1f}. Com isso, essa turma é jovem.") 
elif media >= 26 and media <= 60:
    print(f"A média da idade da turma é {media:.1f}. Com isso, essa turma é adulta.")
else:
    print(f"A média da idade da turma é {media:.1f}. Com isso, essa turma é idosa.")  


#6 – Entrar com nome, nota da prova 1 e nota da prova 2 de N alunos. N é um número inteiro digitado pelo usuário. A cada iteração, imprima o nome do aluno e média arredondada. Caso o usuário digite “FIM”, a estrutura de repetição deve ser interrompida. Ao final, calcule e imprima amédia geral da turma.
soma_notas = 0 
contador_alunos = 0

while True:
    nome = input("Digite o nome do aluno (ou 'FIM' para encerrar): ")
    
    if nome == "":
        break
    
    nota_1 = float(input("Digite a nota da prova 1: "))
    nota_2 = float(input("Digite a nota da prova 2: "))
    
    media = (nota_1 + nota_2) / 2
    media_arredondada = round(media) #round = arredondar um número
    
    print(f"Aluno: {nome}, Média arredondada: {media_arredondada}")
    
    soma_notas += media
    contador_alunos += 1
    
if contador_alunos > 0:
    media_geral = soma_notas / contador_alunos
    print(f"Média geral da turma: {media_geral:.2f}")
else:
    ""

    
     
               
        
    
