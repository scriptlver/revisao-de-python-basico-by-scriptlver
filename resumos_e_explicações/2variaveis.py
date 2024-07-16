# 2. variaveis (armazenar dados em um determinado lugar)
# exemplo, uma caixa que guarda roupas, comidas...

ovos = 10 #("estou dizendo que em um determinado ambiente (caixa) tem 10 ovos")
print("Nessa caixa tem",ovos,"ovos") #coloquei ovos sem aspas para retornar direto ao valor da váriavel

gatos = 3
print("Na minha casa tem",gatos,"gatos")

#tipos de variáveis

#STRING = usado para palavras (SEMPRE USAMOS ASPAS PARA INDICAR UMA STRING), OBS: pode se transformar um número em string, usando aspas, exemplo: "7" (STRING)
nome = "Gabriel" #(string)
print("Meu nome é",nome)
número = "7" #transformei um número em string
print("Número:",número)

#INT = usado para representar números inteiros (NÃO USAMOS ASPAS)
n1 = 8
print(n1)
n2 = (str(13)) #transformei um int em string, usando (str)
print(n2)

#FLOAT = usado para representar números decimais (não utiliza aspas)
numero = 2.3
print(numero)
numero1 = (str(1.2))
print(numero1)

#BOOLEAN = usado para representar valores verdadeiros ou falsos
possui_emprego = True
print(possui_emprego)

esta_desempregado = False
print(esta_desempregado)

#DESCOBRIR O TIPO DE VÁRIAVEL
print(type(nome))
print(type(n1))
print(type(possui_emprego))