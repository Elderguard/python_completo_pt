# DICIONÁRIOS OU MAPAS

#index      0        1        2    ---ordenável
lista = ['item1', 'item2', 'item3']
tupla = ('item1', 'item2', 'item3')

#chave:valor
dicio = {'nome' : 'Gabriel', 'ano' : 1993, 'valorLogico' : True}
print(dicio)

# Uma forma de realizar alterações em uma chave dentro do dicionário é com a seguinte atribuição:
dicio['nome'] = 'Pedro'
print(dicio)

# Outra forma é pela função update
dicio.update({'nome':'Ana'})
print(dicio)

# Também é possível adicionar itens, por meio da atribuição:
dicio['idade'] = 32
print(dicio)

# Ou pela função update
dicio.update({'estado':'Rio de Janeiro'})
print(dicio)