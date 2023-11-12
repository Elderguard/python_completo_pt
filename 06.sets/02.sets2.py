"""
Listas: Coleção ordenada, mutável e que permite valores duplicados
Tuplas: Coleção ordenada, imutável e que permite valores duplicados
Dicionarios: Coleção não-ordenada, mutável e que não permite valores duplicados
Sets: coleção não-ordenada, imutável e que não permite valores duplicados
"""

tupla = (3, 7, 9, 5)
#É possível transformar a tupla em um set utilizando o construtor do set.
#Já vimos anteriormente o construtor de listas: list
#Já vimos anteriormente o construtor de tuplas: tuple
#Já vimos anteriormente o construtor de dicionarios: dict

#O construtor de conjuntos é o set
conjunto = set(tupla)
print(conjunto)
print(type(conjunto))

#Considerando a natureza dos sets, é impossível referenciar elementos dentro e manipulá-los como é feito com as coleções anteriores.
#Para conseguir trabalhar com esse tipo de coleção, é necessário utilizar loops.

conj = {'item1', 'item2', 'item3', 'item4', 'item5'}

# Passará por cada item realizando a impressão.
for x in conj:
    print(x)