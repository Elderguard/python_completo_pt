#Kwargs

"""

def imprimir_nomes(nomes):
    print(nomes)

imprimir_nomes(nomes='ana', sobrenomes='julia')

No exemplo acima, o programa retornaria um erro, pois foram passados mais argumentos do que o que foi definido como parâmetro da função.

"""
# Uma forma de contornar isso é com os KwArgs representados por **

def imprimir_nomes(**nomes):
    print(nomes)


imprimir_nomes(nomes = 'ana', sobrenomes = 'julia')
# Dessa forma é possível utilizar todos os argumentos informados, levando à criação de um DICIONÁRIO que será impresso.

# Pode-se utilizar a impressão da seguinte forma:
def imprimir_nomes(**nomes):
    print(f'{nomes['nome']} {nomes['sobrenome']}')

imprimir_nomes(nome = 'ana', sobrenome = 'julia')

# Ou ainda, declarando o dicionário anteriormente:

dicio = {'nome': 'ana', 'sobrenome': 'julia'}
imprimir_nomes(nome = 'ana', sobrenome = 'julia')