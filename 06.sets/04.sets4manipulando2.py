# Acessando os itens do meu set
set1 = {4,5,7,8,9,1}
set2 = {'item3','item5', 'item1'}

###ADICIONANDO ELEMENTOS###

# Adicionaremos os itens do set2 para o set1
set1.update(set2)
print(set1)

# Podemos também adicionar itens sem estarem previamente em uma variável
set1.update({'item2','item4'})
print(set1)

# A função update tem a capacidade de adicionar itens de qualquer outro tipo de coleção, transformando-as em set também.

# Adicionando uma lista
set1.update([1,4,7,8,9,3]) # Apesar disso os valores duplicados serão ignorados.
print(set1)

# Adicionando uma tupla
set1.update((1,4,7,8,9,3, 'item5', 'item6')) # Os valores duplicados serão ignorados.
print(set1)

###REMOVENDO ELEMENTOS###

# Podemos utilizar a função pop para remover um item:
set1.pop() # Por não ser ordenada, um item aleatório será removido.
print(set1)

print(30*"-")

# Podemos utilizar também a função remove:
set1 = {'item6', 1, 3, 4, 5, 7, 8, 9, 'item3', 'item4', 'item1', 'item5', 'item2'}
print(set1)
print(30*"-")

set1.remove('item5') # Remove o elemento 'item5'
print(set1)
print(30*"-")

#Ou a função discard:
set1.discard('item6')
print(set1)
print(30*"-")

# A diferença entre a função remove e a função discard é que se eu pedir para remover um item que não existe, o programa resultará em um erro, enquanto pedindo para descartar um item que não existe, nada acontecerá.

# del set1 funciona para apagar o conjunto

# É possível limpar o conjunto com a função clear:
set1.clear()
print(set1)
