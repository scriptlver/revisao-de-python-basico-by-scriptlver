contador_n = 0
soma_idades = 0
media = 0
while True:
    idade = int(input("Digite a sua idade (ou -1 para sair do sistema.): "))
    if idade >= 0:
        soma_idades+= idade
        contador_n+= 1
        media = soma_idades / contador_n
    else:
        break
print("A média das idades das",contador_n,f"pessoas é {media:.1f}")

contador_n = 0
soma_imc = 0
media_imc = 0
while True:
    imc = float(input("Digite o seu IMC (ou um número negativo para sair do sistema): "))
    if imc > 0:
        soma_imc+=imc
        contador_n+=1
    else:
        break
media_imc = soma_imc / contador_n
if media_imc < 16.9:
    print("A média dos imcs das",contador_n,f"é de {media_imc:.1f}")
    print("Estão MUITO abaixo do peso! (Situação de alerta!) ")
elif media_imc >= 17 and media_imc <= 18.4:
    print("A média dos imcs das",contador_n,f"é de {media_imc:.1f}")
    print("Estão abaixo do peso! ")
elif media_imc >= 18.5 and media_imc <= 24.9:
    print("A média dos imcs das",contador_n,f"é de {media_imc:.1f}")
    print("Estão no peso normal! ")
else:
     print("A média dos imcs das",contador_n,f"é de {media_imc:.1f}")
     print("Estão acima do peso! ") 
     
lista_numeros = []
somar_numeros = 0
contador = 0
while True:
    entrada = input("Digite o número desejado (ou espaço em branco para sair do sistema.): ")
    if entrada != "":
        numero = float(entrada)
    else:
        break 
    if numero != "":
        lista_numeros.append(numero)
        maior_numero = lista_numeros[0]
        for num in lista_numeros:
           if num > maior_numero:
              maior_numero = num
              print(lista_numeros)
              print("O maior número dessa lista é",maior_numero)
           else:
               print(lista_numeros)
               print("O maior número dessa lista é",maior_numero) 
    else:
        break 
    
    if numero != "":
        lista_numeros.append(numero)
        somar_numeros+=numero
        print(lista_numeros)
        print("")
        print("A soma desses números é",somar_numeros) 
    else:
        break 
              
        
    
        

     