#Parãmetros de uma função

def minha_funcao():
    var = 'maria' #variável local, não acessável fora do bloco
    return var  #retorna o valor, indicando intenção de exportar

#Até o momento o valor não foi exportado para nenhum lugar
var='ana' #define uma variável global var
print(var) #imprime o valor da variável global var

print(minha_funcao()) #imprimir o valor exportado pela funcao

#Parâmetro é o nome dado aos valores utilizados na definição de uma função

"""
def nome_da_funcao (parametro) 
    corpo da função

"""

def nome_da_funcao(parametro):
    print(f"Olá, {parametro}!")

nome = input("Qual é o seu nome? \n")
nome_da_funcao(nome) #Argumento é o nome dado aos valores utilizados na chamada de uma função.