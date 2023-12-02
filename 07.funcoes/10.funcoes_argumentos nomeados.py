#Argumentos nomeados

def imprimir_nome(nome,sobrenome,idade):
    print('nome: ', nome)
    print('sobrenome: ', sobrenome)
    print('idade: ', idade)

               #parametro=valor
imprimir_nome(sobrenome='clara', idade=25,nome='maria') 
#A utilização de argumentos nomeados serve para possibilitar a declaração de parâmetros fora de ordem. Se os parâmetros fossem declarados normalmente com a sequência acima, teríamos nome 'clara', sobrenome '25' e idade 'maria'. porém a utilização do argumento nomeado resolve esse problema.

print(30*"-") #separador

sobrenome = 'Silva'
nome = 'Rodrigo'
idade = 35
            #parametro=valor onde valor é a variável
imprimir_nome(sobrenome=sobrenome, idade=idade,nome=nome) 
