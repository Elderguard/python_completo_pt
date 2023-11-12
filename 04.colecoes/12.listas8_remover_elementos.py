#index      0        1        2 
lista = ["carro", "barco", "avião"]
print("Essa é a lista inicial:")
print(lista)
print(30*"-")

#A função pop chamada sem parâmetro remove o último item da lista.
lista.pop()

print("Essa é a lista após o comando pop sem argumento:")
for x in range(len(lista)):
    print(f"No índice {x}, temos {lista[x]}")
print(30*"-")

lista.append("avião") #adiciona o elemento avião ao fim da lista
print("Retornado o elemento avião por comando append")

#A função pop com um parâmetro indica o índice em que quer remover um elemento.

lista.pop(0) #remove o elemento no índice 0.

print("Essa é a lista após remover com o comando pop o elemento no índice 0:")
for x in range(len(lista)):
    print(f"No índice {x}, temos {lista[x]}")
print(30*"-")

lista.insert(0,"carro") #insere o elemento carro ao índice 1.
print("Retornado o elemento carro ao índice 0 pelo comando insert.")
#É possível remover um elemento específico com o comando remove.

lista.remove("barco")

print("Essa é a lista após usar o camando remove com o parâmetro 'barco':")
for x in range(len(lista)):
    print(f"No índice {x}, temos {lista[x]}")
print(30*"-")

lista.insert(1,"barco") #insere o elemento barco ao índice 1.
print("Elemento barco adicionado pelo comando insert no índice 1.")

for x in range(len(lista)):
    print(f"No índice {x}, temos {lista[x]}")
print(30*"-")
