# 6. OPERADORES DE COMPARAÇÃO:

#IGUALDADE(==):
idade = 18
if idade == 18: #dizer se a variável idade é igual a um valor.
    print("Você tem 18 anos! ")

#DIFERENTE(!=):
idade = 20
if idade != 18: #dizer se o valor da váriavel é diferente do valor proposto
    print("Você não tem 18 anos!") 

#MAIOR QUE(>): #popular na matemática
v1 = 10
v2 = 5
if v1 > v2:
    print("Valor 1 é maior!")
else:
    print("Valor 2 é maior!")      

#MENOR QUE(<): 
v1 = 10 
v2 = 5
if v1 < v2:
    print("Valor 1 é menor!")
else:
    print("Valor 2 é menor!")    

#MAIOR OU IGUAL QUE(>=):
v1 = 10
v2 = 20
if v1 >= v2:
    print("Valor 1 é maior ou igual a Valor 2")
else:
    print("Valor 2 é maior ou igual a Valor 1")  #vinte é maior que 10!
    
#MENOR OU IGUAL QUE(<=):
v1 = 50
v2 = 40
if v1 <= v2:
    print("Valor 1 é menor ou igual a Valor 2")
else:
    print("Valor 2 é menor ou igual a Valor 1") #quarenta é menor que 50!  
                 
    
#AND = "E":
#você vai usar o AND quando as duas alternativas de um condição forem verdadeiras, ou seja, a condição for TOTALMENTE verdadeira ou quando as duas forem falsas, ou seja, TOTALMENTE falsa.
nota = 9.5
if nota >= 9 and nota <=10:
    print("Aprovadissímo! :D") #ele so é aprovadissímo se a nota for igual ou maior que 9 e menor ou igual a 10, ou seja, de 9 a 10.

#OR = "OU":
#você vai usar o OR apenas quando uma das alternativas de uma condição é verdadeira, OU falsa.
nota = 5
if nota >= 4 or nota < 7:
    print("Você tem direito a fazer recuperação!")    
    