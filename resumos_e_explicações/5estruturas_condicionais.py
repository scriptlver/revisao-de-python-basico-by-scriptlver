#5. ESTRUTURAS CONDICIONAIS:
#(verifica se uma informação é verdadeira ou não, se for, vai imprimirse não, vai imprimir outra condição)
idade = 15
if idade == 15:
    print("Você tem 15 anos!")
if idade != 15:
    print("Você não tem 15 anos!")
    
#o exemplo está errado, pois usar dois ifs é considerado falta de organização do código, por isso é melhor usar dessa maneira:

idade = 15
if idade == 15:
    print("Você tem 15 anos!")
elif idade != 15:
    print("Você não tem 15 anos!")

#a condição so será executada se ela for verdadeira

#ELSE: usado para se todas as condições forem falsas

media = 3
if media >= 7:
    print("Parabéns! Você foi aprovado.")
elif media >= 4 and media < 7:
    print("Terá que fazer recuperação!")
else:
    print("Final.")
    
            
        
