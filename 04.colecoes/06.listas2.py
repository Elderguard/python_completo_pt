#É possível armazenar diversos valores em uma lista, separados por vírgula

lista = ["chicago", "queens", "salvador", "pernambuco"]
print(lista)

lista2 = [2, 3, 7, 8, 10]
print(lista2)

lista3 = [2.0, 3.5, 6.3]
print(lista3)

lista4 = [True, False]
print(lista4)

lista5 = [True, "chicago", 2.5, False, 4]
print(lista5)

#indicar :: dentro do colchetes de índice [slicing] informa ao programa para imprimir tudo na lista.
print(lista5[::])

#indicar 1: dentro do colchetes de índice [slicing] informa ao programa para imprimir da lista a partir do índice 1.
print(lista5[1:])

#indicar :3 dentro do colchetes de índice [slicing] informa ao programa para imprimir da lista do início ao índice 3-1, ou seja item na posição 3.
print(lista5[:3])

