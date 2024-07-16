#1 – Crie um dicionário e armazene nele os seus dados: seu nome, sua idade, cor favorita, cidade onde nasceu. Imprima todos os dados usando o padrão chave: valor.
from email.errors import InvalidDateDefect


valor = {"Nome": "Lavinia",
         "Idade": 18,
         "Cor Favorita": "Preto",
         "Cidade": "Campina Grande"
        }
for valor in valor.items():
    print("%s: %s" % (valor[0],valor[1]))

# 2 – Crie um dicionário e armazene nele os dados do usuário: nome, idade, cor favorita e cidade onde nasceu. O usuário deve digitar os valores. Imprima todos os dados usando o padrão chave: valor. 
valor = {}
valor["Nome"] = input("Digite o seu nome: ")
valor["Idade"] = int(input("Digite a sua idade: "))
valor["Cor Favorita"] = input("Digite a sua cor favorita: ")
valor["Cidade onde nasceu"] = input("Digite a cidade onde você nasceu: ")
for valor in valor.items():
    print("%s: %s" % (valor[0],valor[1]))
    
#3 – Crie um programa que, usando dicionário, crie uma agenda de tamanho fornecido inicialmente pelo usuário. Leia os dados de todos os contatos do usuário de forma que a agenda fique completa e por fim imprima todos os contatos.    
contador = 0
valores = {}
while contador < 5:
    contador += 1
    nome = input("Digite o seu nome: ")
    numero = int(input("Digite o seu número: "))

    valores[contador] = {"Nome": nome, "Número": numero}

for chave, valor in valores.items():
    print(f"Contato {chave}:")
    print(f"Nome: {valor['Nome']}")
    print(f"Número: {valor['Número']}")
    print()
    
#4 – Crie um programa que recebe os nomes de dez times (chaves) e a quantidade de pontos que o time conquistou no campeonato (valores). Em seguida, imprima qual foi o time que mais pontuou e qual sua pontuação.    
contador = 0
valores = {}
while contador < 10:
    contador += 1
    nome = input("Digite o nome do time: ")
    pontos = int(input("Digite os pontos do time: "))
    valores[contador] = {"Nome": nome, "Pontos": pontos}

maior_pontuacao = max(valores.values(), key=lambda x: x["Pontos"])
valores_ordenados = sorted(valores.values(), key=lambda x: x["Pontos"], reverse=True)

print("\nTabela Classificatória:")
for posicao, time in enumerate(valores_ordenados, start=1):
    print(f"Posição: {posicao}")
    print(f"Nome: {time['Nome']}")
    print(f"Pontos: {time['Pontos']}")
    print()

#5 – Crie um programa que, usando dicionário, simule um inventário de um jogo. O dicionário deve ser preenchido até o usuário digitar “FIM”. As chaves serão os nomes dos itens, e os valores serão a quantidade de cada item. Depois de preencher o dicionário, imprima todos os dados usando o padrão chave: valor.  
valores = {}
while True:
    item = input("Digite o nome do item: ")
    quantidade = int(input("Digite a quantidade desse item no seu inventário: "))
    
    valores[item] = quantidade
    
    pergunta = input("Gostaria de adicionar mais um item ao seu inventário? (Digite FIM se a resposta for não): ").strip().lower()
    
    if pergunta == "fim":
        break

print("\nInventário:")
for item, quantidade in valores.items():
    print(f"Item: {item}")
    print(f"Quantidade: {quantidade}")
    print()
    
#6 – Crie um dicionário que contenha pelo menos cinco chaves (ex: “maçã”, “banana”, “abacaxi”, “melão”, “mamão”). Os valores representam o preço de cada fruta. Em seguida, imprima todas as chaves do dicionário. O usuário deve, então, digitar quantas frutas ele quer de cada, até digitar “FIM” (ex: “maçã 5”). O programa deve, por fim, dizer qual o valor total da feira. 
contador = 0
valores = {}

while contador < 6:
    contador += 1
    fruta = input(f"Digite o nome da fruta {contador}: ")
    preço = float(input(f"Digite o preço da fruta {contador}: "))
    valores[contador] = {"nome": fruta, "preco": preço}

print("Frutas disponíveis:")
for chave, valor in valores.items():
    print(f"Fruta: {valor['nome']}")
    print(f"Preço: R${valor['preco']:.2f}")
    print()

pergunta = input("Olá, gostaria de comprar alguma fruta disponível? (sim/não): ").strip().lower()
if pergunta == "sim":
    produto = input("Qual produto gostaria? ")
    quantidade = int(input("Qual a quantidade? "))
    if produto in [v['nome'] for v in valores.values()]:  
        total = quantidade * next(v['preco'] for v in valores.values() if v['nome'] == produto)
        print(f"Total a pagar: R${total:.2f}")
    else:
        print("Produto não disponível.")

#7 – Crie um programa que cadastre informações de várias pessoas (nome, idade e cpf) e coloque em um dicionário. Depois remova todas as pessoas menores de 18 anos do dicionário e coloque em outro dicionário. Por fim, imprima os dois dicionários.
valores_1 = {}
valores_2 = {}
while True:
    valores_1["Nome"] = input("Digite o seu nome: ")
    valores_1["Idade"] = int(input("Digite a sua idade: "))
    valores_1["CPF"] = int(input("Digite o seu CPF: "))
    pergunta = input("Olá, gostaria de cadastrar novamente? (se não, coloque FIM) ").strip().lower()
    if pergunta == "fim":
        break
    
    if "Idade" in valores_1 > 18:
        for chave, valor in valores_2.items():
            valores_2[chave] = valor
    else:
        for chave, valor in valores_1.items():
            valores_1[chave] = valor
            
print("Menores de 18 anos:")
for chave, valor in valores_1.items():
    print(f"{chave}: {valor}")  
    print(f"{"Nome"}")         
                    
        
        