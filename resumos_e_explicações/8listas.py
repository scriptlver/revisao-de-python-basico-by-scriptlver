#8. LISTAS EM PYTHON: uma estrutura que você pode adicionar, remover, substituir e várias funções com seus dados! 

#exemplo do supermercado:

#posições em uma lista:
#em python a ordem dos fatores SEMPRE começa em 0
lista_exemplo = ["exemplo","de","uma","lista"]
# 0 - exemplo
# 1 - de
# 2 - uma
# 3 - lista

#adicionar:
lista_feira = [] #criei uma lista vazia
#se eu quiser adicionar produtos para a lista do supermercado a partir do seu NOME, eu uso append.
lista_feira.append("banana") #adicionei "banana" na lista
print(lista_feira)
#se eu quiser adicionar produtos para a lista do supermercado a partir da POSIÇÃO, eu uso insert.
lista_feira.insert(1,"maça") #usei a posição que eu quero e o que eu quero adicionar
print(lista_feira)

#remover:
lista_feira = ["banana","maça"]
#se eu quiser remover produtos da lista do supermercado a partir do seu NOME, eu uso remove.
lista_feira.remove("banana") #vai remover a partir do nome da lista a "banana"
print(lista_feira) #imprime a lista sem banana
#se eu quiser remover produtos da lista do supermercado a partir da sua posição, eu uso pop.
lista_feira.pop(0) #vai tirar "maça" (posição 0) da lista 
print(lista_feira) #vai imprimir a lista completamente vazia

nome = ["M","A","T","H","E","U","S"]
print(len(nome)) #vai contar quantos elementos tem na lista usando len = 7

#acessando elementos:
nome = ["M","A","T","H","E","U","S"]
print(nome[0]) #vai imprimir o que está na posição 0 = "M"
print(nome[3]) #vai imprimir o que está na posição 3 = "H"

#imprimir elementos em uma lista:
lista_produtos = ["escova_de_dente","pasta_de_dente","pente","shampoo"]
for item in lista_produtos:
    print(lista_produtos[2]) #vai imprimir pente que está na posição 2
    #usei o for para percorrer toda a lista

#apagar TODA a lista:
#CLEAR
lista_produtos = ["escova_de_dente","pasta_de_dente","pente","shampoo"]
lista_produtos.clear()
print(lista_produtos) #vai imprimir a lista totalmente vazia
    


