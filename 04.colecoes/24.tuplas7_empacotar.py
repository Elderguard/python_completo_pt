# Quando criamos uma lista ou uma tupla, a atribuição de elementos que realizamos é chamada "empacotar".

# Criamos a variável tupla e empacotamos os elementos 'item1', 'item2', 'item3' que comporão a tupla.
tupla = ('item1', 'item2', 'item3')
print(tupla)

# Tirar os itens da lista é chamado "desempacotar".
(x, y, z) = tupla
print('x: ', x)
print('y: ', y)
print('z: ', z)

# Se tentarmos desempacotar esses elementos em menos variáveis do que a quantidade de elementos, recebemos o erro:
# ValueError: too many values to unpack

# Para realizar o desempacotamento, podemos utilizar o asterisco, identificando uma variável que receberá o excedente.

del x, y, z  # Removendo as 3 variaveis de uma única vez.

(x, *y) = tupla
print('x: ', x) # X terá o valor do primeiro elemento da tupla.
print('y: ', y) # Y terá uma lista de elementos.

# Para realizar o desempacotamento, podemos utilizar o asterisco, identificando uma variável que receberá o excedente.

del x, y  # Removendo as 2 variaveis de uma única vez.

tupla = ('item1', 'item2', 'item3', 'item4', 'item5')
(x, *y, z) = tupla
print('x: ', x) # X terá o valor do primeiro elemento da tupla.
print('y: ', y) # Y terá uma lista de elementos.
print('z: ', z) # Z terá o último elemento da tupla