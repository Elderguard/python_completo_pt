# Concatenação de tuplas

tupla = ('item1',)
tupla2 = ('a', 'b')

# É possível unir os elementos de tuplas
tupla = tupla + tupla2
print(tupla)

# É possível multiplicar os elementos dentro da tupla, repetindo o valor várias vezes.
tupla = ('item1',)
tupla = tupla * 3
print(tupla)

# A multiplicação da tupla criará a repetição do elemento, não uma operação matemática.
tupla = (3,)
tupla = tupla * 3
print(tupla)

# Voltando à tupla com string.
tupla = ('item1', 'item2', 'item3')
print(tupla)

# Looping para imprimir os elementos da tupla:
for x in tupla:
    print(x)

# Looping para imprimir os index da tupla:
for x in range(len(tupla)):
    print(x)

# Looping para imprimir os elementos a partir do index da tupla:
for x in range(len(tupla)):
    print(x, tupla[x])
