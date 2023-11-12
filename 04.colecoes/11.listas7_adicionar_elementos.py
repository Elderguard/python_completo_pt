#index      0        1        2 
lista = ["carro", "barco", "avião"]
print(lista)
print(len(lista))

#adicionar novos elementos ao fim da lista
lista.append("moto")
print(lista)
print(len(lista))

for x in range(len(lista)):
    print(f"No índice {x}, temos {lista[x]}")

#O comando append aceita apenas um elemento por vez, se tentarmos adicionar múltiplos elementos de uma vez, o programa informará um TypeError.           
#lista.append("moto", "navio", "bicicleta")
#se o interesse é de adicionar múltiplos elementos, deve-se então transformar tudo em um único elemento, ou seja, uma lista.

lista.append(["bicicleta", "navio"])
print(lista)
print(len(lista))

for x in range(len(lista)):
    print(f"No índice {x}, temos {lista[x]}")
    #Porém, isso fará com que os múltiplos itens adicionados sejam adicionados todos ao índice 4, ou seja, uma lista dentro de outra lista. O que pode não ser a intenção neste procedimento.

lista.pop(4) #Remove o item no índice 4
print(lista)

#A função insert consegue receber 2 argumentos. Neste exemplo, adicionaremos o elemento "bicicleta" no índex 1. Isso "empurrará" os itens posteriores para os índices seguintes.
lista.insert(1, "bicicleta")
for x in range(len(lista)):
    print(f"No índice {x}, temos {lista[x]}")

lista.pop(1) #remove o item no índice 1 "bicicleta"

#Para adicionar múltiplos itens sem queeles sejam adicionados em lista, devemos utilizar o comando extend.
lista.extend(["bicicleta","navio"])
for x in range(len(lista)):
    print(f"No índice {x}, temos {lista[x]}")
