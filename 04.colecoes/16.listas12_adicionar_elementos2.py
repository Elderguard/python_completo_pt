lista = ["a", "b", "c"]
lista2 = [1, 4, 6]
print(f"A lista 1 é: {lista}")
print(f"A lista 2 é: {lista2}")
print(30*"-")

#Para unir duas listas, podemos utilizar o operador de soma como comando de concatenação.
lista = lista + lista2
print(f"A lista 1 após concatenação é: {lista}")
print(30*"-")

#Retorna a lista ao valor inicial
lista = ["a", "b", "c"]
print(f"A lista 1 retorna ao valor: {lista}")
print(30*"-")

#Podemos utilizar também a função extend
lista.extend(lista2)
print(f"A lista 1 após função extend: {lista}")
print(30*"-")

#Retorna a lista ao valor inicial
lista = ["a", "b", "c"]
print(f"A lista 1 retorna ao valor: {lista}")
print(30*"-")

#Podemos também utilizar a função append dentro de um loop
for x in lista2:
    lista.append(x)
print(f"A lista 1 após o loop de append: {lista}")
print(30*"-")


