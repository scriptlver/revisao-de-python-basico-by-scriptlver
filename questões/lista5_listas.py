#0 – Crie um programa que leia N frutas e depois as imprima, uma por uma.
lista_frutas = []
while True:
    print("")
    fruta = input("Digite a fruta que você quer adicionar: ")
    print("")
    if fruta != "":
        lista_frutas.append(fruta)
        print("Frutas adicionadas na lista: ")
        for fruta in lista_frutas:
          print(fruta)
    else: 
        break

#1 – Crie um código que permita somar todos os N elementos de uma lista. O usuário deve digitar os números da lista. Não utilize a função sum().  
somar_numeros = 0
lista_numeros = []
while True:
    print("")
    numero = float(input("Digite o número que quer adicionar na lista (ou espaço em branco para sair): ")) 
    if numero != "":
        lista_numeros.append(numero)
        somar_numeros+=numero
        print(lista_numeros)
        print("")
        print("A soma desses números é",somar_numeros) 
    else:
        break    

#2 – Crie um programa que lê N números e imprime o maior deles.
lista_numeros = []
while True:
    entrada = input("Digite o número que deseja adicionar na lista (ou espaço em branco para sair): ")
    if entrada != "":
        numero = float(entrada)
    else:
        break 
    if numero != "":
        lista_numeros.append(numero)
        maior_numero = lista_numeros[0]
        for num in lista_numeros:
           if num > maior_numero:
              maior_numero = num
              print(lista_numeros)
              print("O maior número dessa lista é",maior_numero)
           else:
               print(lista_numeros)
               print("O maior número dessa lista é",maior_numero) 
    else:
        break 

#3 – Crie um programa que lê N strings e imprime o tamanho de cada uma delas. Por fim, imprima também a maior string.
lista_strings = []
while True:
    string = input("Digite a string (ou espaço em branco para encerrar): ")
    
    if string != "":
        lista_strings.append(string)
    else:
        break
if lista_strings: 
    maior_string = lista_strings[0]
    for string in lista_strings:
        if len(string) > len(maior_string):
            maior_string = string
    print(lista_strings)        
    print("A maior string dessa lista é", maior_string, "com", len(maior_string), "letras")
else:
    print("")
    
#4 – Crie um programa que lê 10 números inteiros. Caso o número não tenha sido lido antes, ele é adicionado a uma lista. Caso já tenha sido lido, o número não é adicionado.
lista_numeros = []
while True:
    entrada = input("Digite o número inteiro para adicionar à lista (ou espaço em branco para sair): ")
    if entrada != "":
        numero = int(entrada)
    else:
        break
    if numero in lista_numeros:
        print("Número já adicionado, tente novamente.")
    else:
        lista_numeros.append(numero)
        print(f"Número {numero} adicionado à lista.")
        print(f"Lista: {lista_numeros}") 
        
#5 – Crie um programa que lê uma lista de 8 números. Em seguida, imprima o produto de todos os números. 
lista_numeros = []
produto = 1
while True:
    entrada = input("Digite o número inteiro para adicionar à lista (ou espaço em branco para sair): ")
    if entrada == "":
        break
    else:
        numero = float(entrada)
        if numero != "":
           lista_numeros.append(numero)
           produto*=numero
           print(produto)
        else:
            break

#6 – Crie um programa que recebe N nomes. Após digitar os nomes, o usuário pode consultar se algum nome específico foi lido. Caso tenha sido lido, o programa responde “Encontrado”, caso não, responde “Não encontrado”. O programa é finalizado quando o usuário digita “FIM”.
lista_nomes = []

while True:
    nome = input("Digite o nome (programa encerrado quando digitar FIM): ")
    if nome.strip().lower() == "fim":
        break 
    
    lista_nomes.append(nome)
    print(lista_nomes)
    
    pergunta = input("Você gostaria de procurar por algum nome? (sim/não): ").strip().lower()
    if pergunta == "sim":
        nome_buscar = input("Digite o nome que deseja buscar: ")
        if nome_buscar in lista_nomes:
            print(f"{nome_buscar} encontrado na lista.")
        else:
            print(f"{nome_buscar} não encontrado na lista.")
            
    else:
        print("FIM.")
        break 
print("Tchau.")

#7 – Crie um programa que permita intercalar os elementos de duas listas de N elementos digitadas pelo usuário. As duas listas terão o mesmo comprimento. Imprima a lista intercalada de uma só vez. Exemplo: Intercalar as listas: L1 = ["a", "b", "c", "d"] e L2 = [10, 20, 30, 40] resultaria em [“a”, 10, "b", 20, "c", 30, "d", 40]
lista_letras = []
lista_numeros = []
while True:
    letra = input("Digite a letra desejada para adicionar na lista: ")
    if letra != "":
        lista_letras.append(letra)
    else:
        break
    entrada = input("Digite o número desejado: ")
    if entrada == "":
        break
    else:
        numero = float(entrada)
        if numero != "":
           lista_numeros.append(numero)
        else:
            break
    lista_intercalada = []
    for i in range(len(lista_letras)):
        lista_intercalada.append(lista_letras[i])
        lista_intercalada.append(lista_numeros[i])       
           
                      
    
         
                