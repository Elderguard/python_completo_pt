#É possível armazenar diversos valores em uma lista, separados por vírgula

lista = ["gato", "cachorro", "peixe", "cavalo", "tubarão", "girafa"]
print(lista)

print(type(lista)) #retorna o tipo da lista class 'list'
print(lista[1]) #imprime apenas o valor no índice 1 da lista

#modificar itens da lista
lista[1] = 'cavalo'
print(lista)

#modificando vários itens de uma vez
lista[1:4] = ["águia", "morcego", "elefante"]
print(lista)

#informando apenas a partir do item 1 até (2-1), ou seja apenas um elemento, porém atribuindo 2 elementos. O elemento informado é substituído por 2 novos elementos a partir daquela posição.
lista[1:2] = ["águia", "elefante"]
print(lista)
print(len(lista))

#informando uma sequência grande, porém informando apenas um elemento fará com que os elementos excedentes sejam apenas removidos.
lista[1:5] = ['tubarão']
print(lista)
print(len(lista))