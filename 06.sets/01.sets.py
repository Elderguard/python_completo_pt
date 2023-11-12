"""
Listas: Coleção ordenada, mutável e que permite valores duplicados
Tuplas: Coleção ordenada, imutável e que permite valores duplicados
Dicionarios: Coleção não-ordenada, mutável e que não permite valores duplicados
Sets: coleção não-ordenada, imutável e que não permite valores duplicados
"""

#Os sets também são conhecidos como conjuntos
conjunto = {'item1', 'item2', 'item3'}
print(type(conjunto)) #<class 'set'>
print(conjunto) # Verificar que a ordem de impressão não é necessariamente a mesma da atribuição.

# Imprimir o tamanho do conjunto:
print(len(conjunto))

#Reatribuindo com valores repetidos:
conjunto = {'item1', 'item2', 'item3', 'item3', 'item1', 'item2'}
print(conjunto) #Verifique que os itens repetidos serão descartados.

#Reatribuindo com tipos diferentes:
conjunto = {'item1', 3, True, 4.7, 'são paulo'}
print(type(conjunto))
print(conjunto)
print(len(conjunto))