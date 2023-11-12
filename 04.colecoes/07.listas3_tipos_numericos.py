#É possível armazenar diversos valores em uma lista, separados por vírgula

lista = ["chicago", "queens", "salvador", "pernambuco"]
print(lista)

lista2 = [2, 3, 7, 8, 10]
print(lista2)

lista3 = [2.0, 3.5, 6.3]
print(lista3)

#É possível unir/somar duas listas;
lista2 = lista2 + lista3
print(f"A lista2 após unir com a lista 3 é: {lista2}")

#É possível usar uma função que encontra automaticamente o tamanho da lista
print("A quantidade de elementos na lista 1 é: ", len(lista))
print("A quantidade de elementos na lista 2 é: ", len(lista2))

lista4 = ["Nome", "Nome2", "Nome"]
print("A quantidade de elementos na lista 4 é: ", len(lista4))

#FUNÇÕES QUE SÓ PODEM SER UTILIZADAS COM TIPOS NUMÉRICOS

#Somatório dos elementos da lista
print("A soma da lista2 é: ", sum(lista2))

#Maior valor, retorna o elemento de valor máximo da lista
print("O maior valor é: ",max(lista2))

#Menor valor, retorna o elemento de valor mínimo da lista
print("O menor valor é: ", min(lista2))