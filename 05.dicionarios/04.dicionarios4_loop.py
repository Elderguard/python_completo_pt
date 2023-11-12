# DICIONÁRIOS OU MAPAS

# index      0        1        2    ---ordenável
lista = ['item1', 'item2', 'item3']
tupla = ('item1', 'item2', 'item3')

# chave:valor
dados = {'nome' : 'Gabriel', 'ano' : 1993, 'valorLogico' : True}
dados.update({'estado':'Rio de Janeiro'})
print(dados)

# Se utilizarmos um loop através do dicionário para impressão, teremos a impressão das chaves.
for x in dados:
    print(x)
print(30*"-")

# Se quisermos imprimir os elementos de cada chave, precisamos de outra sintaxe.
for x in dados:
    print(dados[x])
print(30*"-")

# Também podemos utilizar a função values para isso:
for x in dados.values():
    print(x)
print(30*"-")

# Ou para imprimir as chaves:
for x in dados.keys():
    print(x)
print(30*"-")

# Ou também com a função items, retornando as tuplas dentro do dicionario:
for x in dados.items():
    print(x)
print(30*"-")

# Ainda com a função items, retornando os valores das tuplas dentro do dicionario, separadamente:
for x, y in dados.items():
    print(x, y)
print(30*"-")

# É possível ainda utilizar a função copy com dicionários:
dicio = dados.copy()
print(dicio)

# Outra forma de fazer essa cópia é utilizando o comando dict
dicio2 = dict(dados) #cria um novo dicionário com base em "dados"
print(dicio2)
print(30*"-")

dados['idade'] = 27
print(dados)
print(dicio)
print(dicio2)


