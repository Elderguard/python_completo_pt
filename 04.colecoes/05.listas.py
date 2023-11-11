#É possível armazenar diversos valores em uma lista, separados por vírgula

lista = ["chicago", "queens", "salvador", "pernambuco"]
print(lista)

lista2 = [2, 3, 7, 8, 10]
print(lista2)

lista3 = [2.0, 3.5, 6.3]
print(lista3)

lista4 = [True, False]
print(lista4)

#python é capaz de armazenar tipos diferentes de dados em uma mesma lista, o que não costuma acontecer em outras linguagens.
lista5 = [True, "chicago", 2.5, False, 4]
print(lista5)

#imprime o tipo da lista 5
print(type(lista5))

#imprime o valor no índice 1 da lista 5
print(lista5[1])

#imprime o valor contando de trás para frente
print(lista5[-1])

