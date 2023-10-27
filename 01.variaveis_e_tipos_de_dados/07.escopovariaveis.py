"""escopo de variaveis"""


"""
as variaveis globais

as variaveis locais
"""

x = 5 #variavel global

def funcao(): #cria a função com o nome "funcao"
    x = 3 #variavel local - não vai sobrescrever a global, só existe na função
    print("Valor da variavel local: ", x)

funcao() #chama a função existente "funcao"
print("Valor da variavel global: ", x)

y = 'Gabriel'             #nome
z = 1.74                  #altura
t = "000.000.000-00"      #cpf
l = 23                    #idade
#apesar de o exemplo acima estar bem legível, não é a melhor forma.
#a melhor forma seria usar o nome da variavel para isso

nome = "Gabriel"
altura = 1.74
cpf = "000.000.000-00"
idade = 23