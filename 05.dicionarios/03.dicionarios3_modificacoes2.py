# DICIONÁRIOS OU MAPAS

# index      0        1        2    ---ordenável
lista = ['item1', 'item2', 'item3']
tupla = ('item1', 'item2', 'item3')

# chave:valor
dados = {'nome' : 'Gabriel', 'ano' : 1993, 'valorLogico' : True}
dados.update({'estado':'Rio de Janeiro'})
print(dados)

# Os dicionários tem uma função para remover itens, popitem.
#Este comando só existe a partir da versão 3.7 do python.
dados.popitem() # Remove o último item do dicionário
print(dados)
# Nas outras versões, abaixo da 3.7, essa função elimina um item aleatório.

# Retornando o item que foi removido.
dados.update({'estado':'Rio de Janeiro'})
print(dados)

# Também é possível utilizar a função pop, definindo a chave que quer remover.
dados.pop("estado")
print(dados)

# Retornando o item que foi removido.
dados.update({'estado':'Rio de Janeiro'})
print(dados)

# É possível ainda utilizar o comando del:
del dados['estado']
print(dados)
# del dados também pode ser utilizado para remover a variável por completo

# Retornando o item que foi removido.
dados.update({'estado':'Rio de Janeiro'})
print(dados)

# É possível ainda utilizar o comando clear nos dicionários:
dados.clear()
print(dados)
