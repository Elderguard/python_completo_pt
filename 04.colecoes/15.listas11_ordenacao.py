carrinhoDeCompras = ["pão", "carne", "verduras", "alface"]
print("Essa é a lista inicial:")
print(carrinhoDeCompras)

for x in range(len(carrinhoDeCompras)):
    print(f"No índice {x}, temos {carrinhoDeCompras[x]}")
print(30*"-")

#É possível manipular a ordenação da lista com o comando sort.
carrinhoDeCompras.sort()

print("Essa é a lista após a função sort: ")
print(carrinhoDeCompras)

for x in range(len(carrinhoDeCompras)):
    print(f"No índice {x}, temos {carrinhoDeCompras[x]}")
print(30*"-")

#OBS também funciona com números.
lista = [1, 50, 23, 67, 100]
print(lista)
print(30*"-")

#Ordenamos a lista.
lista = lista
lista.sort()
print(f"Lista ordenada de forma crescente: {lista}")
print(30*"-")

#Também é possível inverter a ordenação para decrescer.
lista = lista
lista.sort(reverse=True)
print(f"Lista ordenada de forma decrescente: {lista}")
print(30*"-")

#Voltando a lista ao estado inicial.
lista = [1, 50, 23, 67, 100]
print(lista)
print(30*"-")

#É possível inverter a ordem atual da lista sem realizar uma nova ordenação crescente ou decrescente, apenas considerando a situação atual dela.
lista.reverse()
print(lista)
print(30*"-")

#Criamos uma lista com nomes onde os nomes iniciam com letra maiúscula, porém dois dos nomes inicia com letra minúscula e faremos a ordenação crescente.
lista = ["Ana", "Pedro", "Marta", "Clarice", "beatriz", "ana clara"]
print(lista)
print(30*"-")

#Ordenação crescente
lista.sort() 
#A ordenação colocará todos os nomes que iniciam em maiúsculo primeiro e os que iniciam em minúsculo ao final.
print(lista)
print(30*"-")

#Para resolver esse problema, criaremos uma chave nos parâmetros da função sort.

lista.sort(key = str.lower) 
#Essa chave indicará para tratar todos os caracteres igualmente como letras minúsculas.
print(lista)