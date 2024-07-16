#1 – Faça um código que recebe uma frase e retorna o número de palavras que a frase contém.
frase = input("Digite a frase desejada: ")
frase_espaço = frase.split()
print(len(frase_espaço))

#2 – Faça um algoritmo que recebe uma frase e substitui todas as ocorrências de espaço por “#”.
frase = input("Digite a frase: ")
print(frase.replace("","#"))

#3 – Faça um programa que leia o nome do usuário e o imprima na vertical, em forma de escada, usando apenas letras maiúsculas.
nome = input("Digite seu nome: ")
nome = nome.upper()
for i in range(len(nome)):
    substring = nome[:i+1]
    print(substring)
    
#4 – Faça um programa que decida se duas strings lidas do teclado são palíndromas mútuas, ou seja, se uma é igual à outra quando lida de trás para frente.  
string1 = input("Digite algo: ")
string2 = input("Digite algo: ")

string1_tr = string1[::-1]
string2_tr = string2[::-1]

if string1_tr == string2_tr:
    print("Elas são palíndromas. ")
else:
    print("Não são iguais. ")    

#5 – Faça um programa que leia o nome do usuário e mostre o nome de trás para frente, utilizando somente letras maiúsculas.
nome_de_usuario = input("Digite o nome de usuario: ")
nome_upper = nome_de_usuario.upper()
print(nome_upper[::-1])

#6 – Um anagrama é uma palavra que é feita a partir da transposição das letras de outra palavra ou frase. Por exemplo, “Iracema” é um anagrama para “America”. Escreva um programa que decida se uma string é um anagrama de outra string, ignorando os espaços em branco. O programa deve considerar maiúsculas e minúsculas como sendo caracteres iguais, ou seja, “a” = “A”.
str1 = input("Digite a primeira string: ")
str2 = input("Digite a segunda string: ")

str1_clean = str1.replace(" ", "").lower()
str2_clean = str2.replace(" ", "").lower()

str1_sorted = ''.join(sorted(str1_clean))
str2_sorted = ''.join(sorted(str2_clean))

if str1_sorted == str2_sorted:
    print(str1,"e",str2 ,"são anagramas!")
else:
    print(str1,"e",str2,"não são anagramas.")

    
