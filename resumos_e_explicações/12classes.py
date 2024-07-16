#12. CLASSES: 
#uma classe agrupa metódos e váriaveis para extrair várias instâncias daquela classe

class Conta: #criação da classe conta com os parâmetros para criar uma conta (agencia, conta, saldo e titular)
    agencia = 0
    conta = 0
    saldo = 0.0
    titular = ""
    
    def __init__(self,a,c,s,t): #metodo usado para inicializar e retornar os parâmetros da classe conta
        self.agencia = a
        self.conta = c
        self.saldo = s
        self.titular = t
        
novaConta = Conta(1829,223,9201,"Luiz Ribeiro") #dados do usuario relacionados com os parâmetros(agencia, conta, saldo e titular) 
print(novaConta.agencia) 
print(novaConta.conta)
print(novaConta.saldo)
print(novaConta.titular)
     
    
    

