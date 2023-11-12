conjunto1 = {1,5,8,9}
conjunto2 = {3,6,2}

# Realizar a união de conjuntos

conjunto3 = conjunto1.union(conjunto2)
print(conjunto3)
print(type(conjunto3))

del conjunto3

# Reatribuindo os valores
conjunto1 = {1,5,3,2}
conjunto2 = {3,6,2} # Dois valores se repetem nos conjuntos

# Criando a intersecção de conjuntos
conjunto3 = conjunto1.intersection(conjunto2)
print(conjunto3)

del conjunto3

# Usando Intersection_update é possível atualizar o conjunto para apenas os valores de intersecção:
conjunto1.intersection_update(conjunto2)
print(conjunto1)

# Reatribuindo o valor inicial do conjunto 1:
conjunto1 = {1,5,3,2}

# Novo conjunto com os valores que não se repetem:
conjunto3 = conjunto1.symmetric_difference(conjunto2)
print(conjunto3)

del conjunto3

# Usando symmetric_difference_update é possível atualizar o conjunto para apenas os valores que não se repetem:
conjunto1.symmetric_difference_update(conjunto2)
print(conjunto1)

#DIAGRAMA DE VENN - referência