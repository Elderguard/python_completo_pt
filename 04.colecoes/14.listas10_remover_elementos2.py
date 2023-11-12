#index      0        1        2 
lista = ["carro", "barco", "avião"]
print("Essa é a lista inicial:")
print(lista)
print(30*"-")

#A função del pode ser usada para apagar um elemento da lista.
del lista[0]

print("Essa é a lista após o comando del lista[0]:")
print(lista)

for x in range(len(lista)):
    print(f"No índice {x}, temos {lista[x]}")
print(30*"-")

del lista

carrinhoDeCompras = ["pão", "carne", "verduras"]

print(carrinhoDeCompras)

for x in range(len(carrinhoDeCompras)):
    print(f"No índice {x}, temos {carrinhoDeCompras[x]}")
print(30*"-")

#Se eu quiser limpar uma lista, apagando todos os elementos mas com a intenção de que a lista continue existindo, devemos usar a função clear.
carrinhoDeCompras.clear()
print("Esse é o carrinho após usar a função clear: ")
print(carrinhoDeCompras)
for x in range(len(carrinhoDeCompras)):
    print(f"No índice {x}, temos {carrinhoDeCompras[x]}")
    #Esse loop nem terá resultado no console, não há elementos para executar a condição.
print(30*"-")

carrinhoDeCompras.extend(["pão", "carne", "verduras"])
print("Itens adicionados novamente com comando extend.")
print(carrinhoDeCompras)
print(30*"-")