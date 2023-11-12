lista = ["a", "b", "c"]
print(f"Esta é a lista1: {lista}")

lista2 = lista
print(f"Esta é a lista2: {lista2}")

#Adicionando elemento na lista 2
lista2.append("d")
print(f"Esta é a lista1 após append na lista 2: {lista}")
print(f"Esta é a lista2 após append na lista 2: {lista2}")

#A atribuição anterior não atribui apenas os mesmos valores, mas o mesmo endereçamento de valores, logo se eu alterar a lista 2, a lista 1 também será alterada.

#removendo último item
lista2.pop()
print(f"Esta é a lista1 após pop na lista 2: {lista}")
print(f"Esta é a lista2 após pop na lista 2: {lista2}")

#Outra forma de copiar uma lista é usar a função copy
lista2 = lista.copy()
print(f"Esta é a lista1 após função copy na lista 2: {lista}")
print(f"Esta é a lista2 após função copy na lista 2: {lista2}")

#Adicionando elemento na lista 2
lista2.append("d")
print(f"Esta é a lista1 após append na lista 2: {lista}")
print(f"Esta é a lista2 após append na lista 2: {lista2}")

#Adicionando elemento na lista 1
lista.append("e")
print(f"Esta é a lista1 após append na lista 1: {lista}")
print(f"Esta é a lista2 após append na lista 1: {lista2}")