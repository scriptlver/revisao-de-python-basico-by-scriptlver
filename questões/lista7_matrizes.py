#1 – Crie uma matriz 3 x 3. Preencha a matriz com o valor 0. Imprima a matriz de forma simplificada.
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for linha in matriz:
  print(linha)

#2 – Crie uma matriz 3 x 3. Utilizando um contador, preencha a matriz com os valores de 1 até 9. Imprima a matriz separando as linhas. 
contador = 1
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(contador)
        contador+=1
    matriz.append(linha)
for linha in matriz:
    print(linha)        

