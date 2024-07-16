#10. STRINGS:
#METODOS E OPERAÇÕES COM STRINGS:

#len: ele serve para saber o tamanho da string
nome = "Gabriel"
print(len(nome)) #vai imprimir a quantidade de letras que tem no nomr Gabriel (7)

#for: ele serve para listar os caracteres de uma string
nome = "Luiz"
for letra in nome:
    print(letra) #vai imprimir cada letra do nome 

#s2 in s1: conferir se os caracteres de s1 estão em s2
nome = "Larissa"
print("Lar" in nome) #imprime TRUE se for verdadeiro e FALSE se for falso

#string lower: converte a string toda para minusculo
fruta = "BaNANA"
print(fruta.lower())

#string upper: converte a string para maiusculo
fruta = "morango"
print(fruta.upper())

#string count: verifica quantas vezes a letra foi repetida
nome = "João"
print(nome.count("o"))

#string is numeric: verifica se a string tem números
nome = "Cássio1"
print(nome.isnumeric()) #imprime FALSE pq a string não é composta APENAS de números, agr se tiver só número é TRUE

#string is alpha: verifica se a string é composta por letras
numero = "123"
print(numero.isalpha()) #imprime FALSE pq so tem números

#string split: quebra a string por espaço
frutas = "banana maçã"
print(frutas.split())

#string replace: substitui um texto por outro
fruta = "laranja"
print(fruta.replace("laranja","banana"))

#string join: mistura strings
linguagens = "python"
print(linguagens.join("java"))

#string starts with: verifica se o nome inicia a string
nome = "Ana"
if nome.startswith("A"):
    print("True")
else:
    print("False")

#string + string: junta strings
nome ="Carlos"
sobrenome = " Alberto"
nome_completo = nome + sobrenome
print(nome_completo)

#string * int: repete a string N vezes
nome = "Laila"
print(nome*5)    

#string capitalize: primeira letra maiuscula e o resto minusculo
nome = "eduardo"
print(nome.capitalize())

#string find: verifica a posição da string
nome = "Amanda"
print(nome.find("manda"))


