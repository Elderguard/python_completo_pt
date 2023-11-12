#Em uma lista, podemos alterar o valor de um índice
lista = ['item1', 'item2']
print(lista)

lista[0] = 'item3'
print(lista)

#Porém se realizarmos um mesmo procedimento na tupla, teríamos um erro.
tupla = ('item1', 'item2')
print(tupla)
# tupla[0] = 'item3'
# print(tupla)
#O código comentado acima gera no console o erro:
#TypeError: 'tuple' object does not support item assignment

#Apesar disso, a tupla ainda pode ser sobrescrita com uma nova atribuição de valor:
tupla = ('item3', 'item4', 'verde')
print(tupla)