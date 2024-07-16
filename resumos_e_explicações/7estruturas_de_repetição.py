#7. ESTRUTURAS DE REPETIÇÃO (RANGE,FOR E WHILE):
#RANGE x FOR: usada para sequências de repetição

for i in range(5): #vai imprimir os números de 0 a 4 (pois começa do zero, com isso imprimindo 5 números)
    print(i)

for i in range(1,11): #imprimi os números de 1 a 10 
    print(i)    
 
for i in range(0,11,2): #imprimi os números de 0 a 10 pulando 2
    print(i)    

frutas = ["banana","maça","pera"]
for fruta in frutas:
    print(len(frutas)) #contar a quantidade de frutas na lista

numero = [0,2,4,6,8,10]
soma = 0
for num in numero:
    soma = soma + num
print(soma) #vai imprimir a soma de todos os números

#RANGE x WHILE: "enquanto...."
contador = 5
while contador > 0:
    print(contador) #vai imprimir uma contagem regressiva
    contador -= 1
    
numero = 1
while numero <= 10:
    print(numero) #imprimir os números de 1 a 10
    numero += 1 
    
opção = 0
while opção != "3":
    print("1) Saque, 2) Extrato, 3) Sair")
    opção = input("Digite a opção desejada: ")
print("Tchau!")              


 