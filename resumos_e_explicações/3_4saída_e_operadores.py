#3. saída de dados
salario = 1150.40 #float, valor decimal
print("Salário: R$",salario) #usando print para imprimir o valor da váriavel salário

#e se quando eu usar um valor float e ele tiver várias casas decimais, como posso diminui-las?
imc = 21.4594 #float
print("IMC: %.1f" % imc) #vai imprimir 21.5 (apenas uma casa decimal depois do ponto) 

# %.s (substitui strings), %.d (substitui inteiros), %.f (substitui floats)

#4. OPERADORES MATEMÁTICOS!
n1 = 10
n2 = 5 #n1,n2 = declarando váriaveis

#SOMA:
soma = n1 + n2
print(soma) #imprimi justamente 15

#SUBTRAÇÃO:
sub = n1 - n2
print(sub) #imprimi justamente 5

#MULTIPLICAÇÃO:
mult = n1 * n2 #em python usamos * para representar o x da multiplicação
print(mult) #imprimi 50

#DIVISÃO:
div = n1/n2 #usamos / para dividir números em python
print(div) #imprimi 2.0

#ATENÇÃO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DIVISÃO INTEIRA
#usadas para qualquer tipo de número, principalmente os inteiros
div_int = n1 // n2
print(div_int) #imprimi 2 (por ser inteiros, imprimi um valor inteiro)

#RESTO DE DIVISÃO:
resto_div = n1 % n2 #imprimir o valor que vai sobrar no resto de uma divisão se o resultado não for inteiro
print(resto_div) #imprimi 0, pois 10 é divisivel por 5 (vai dar 2)
#extra:
n3 = 10
n4 = 4
resto_div = n3 % n4
print(resto_div) #imprimi 2, pois quando faz 10 / 4, sobra 2 no resto de divisão

#POTÊNCIA:
pot = n1 ** n2 #pega o primeiro número e eleva o segundo
print(pot) #10*10*10*10*10 (5 vezes)

#O operador de soma pode ser usado tanto para strings quanto para números
nome = "Luis"
sobrenome = " Alves" #espaço antes para não imprimir colado
nome_completo = nome + sobrenome
print(nome_completo)

nome = "Matheus"
idade = (str(19)) #transformar em string, pois uma string so pode ser somada a outra, como um int so pode ser somado com outro
nome_e_idade = nome + idade
print(nome_e_idade)


