#9. ESTRUTURAS DE DADOS(TUPLAS, DICIONARIOS X MATRIZES):
#TUPLAS: usadas para adicionar dados (como listas), a unica diferença é que não pode modificar a lista com esses dados
tupla1 = ("Luiz","José","André","João")
print(tupla1) #não pode modificar esses dados
tupla_erro = (9,3,4,5,6)
tupla_erro[1] = 2
print(tupla_erro) #vai dar erro, pois não pode substituir um dado por outro em uma tupla

#DICIONÁRIO: uma lista que guarda valores de um valor, exemplo: PB = Paraíba
estados = {"PB": "Paraíba","PE": "Pernambuco"}

#criando um dicionário:
estados = dict({
    "PB": "Paraíba",
    "PE": "Pernambuco",
    "SP": "São Paulo"  
})
print(estados)

siglas = {} #dicionário vazio
siglas["SAMU"] = "Serviço de Atendimento Móvel de Urgência"
siglas["CLT"] = "Consolidação das Leis do Trabalho"
siglas["ONU"] = "Organização das Nações Unidas"
print(siglas["SAMU"]) #vai imprimir = Serviço de Atendimento Móvel de Urgência

#excluindo dicionários:
#popitem = 
elemento_eliminado = siglas.popitem()
print(elemento_eliminado) #remove o ultimo item do dicionário e retorna como tupla(com os parentêses)

#pop =
elemento_eliminado = siglas.pop("SAMU")
print(elemento_eliminado) #remove o que tem dentro de SAMU e retorna depois sozinho

#clear =
siglas.clear()
print(siglas) #apaga tudo do dicionário

#percorrendo um dicionário:
dados = {"Nome":"Luiz",
         "Idade": 18,
         "Cidade": "São Paulo",
         "Região": "Sudeste"
         }
for dado in dados.items():
    print("%s: %s" % (dado[0],dado[1])) #vai imprimir o dicionario mais organizado

#MATRIZES:
matriz = [[1,2,3],[4,5,6],[7,8,9]] #123
                                   #456
                                   #789
#acessando uma matriz:
matriz = []
n_linhas = int(input())
n_colunas = int(input())  
for i in range(n_linhas):
    linha = []
    for j in range(n_colunas):
        linha.append(j) 
    matriz.append(linha)  

print(matriz)
                                          
