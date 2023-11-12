# E se quisermos alterar os valores da tupla, por algum motivo?

tupla = ('item1', 'item 2', 'item3', 'item4') # Apesar de os parênteses não serem obrigatórios, é comum manter sua utilização por questões de formatação e leitura de código por outras pessoas.

# Devemos criar uma lista que receberá os valores da tupla.
lista = list(tupla)

print(tupla)
print(lista)

#Agora é possível trabalhar com estes valores a partir da lista.
lista.append('item5')
print(lista)

#Porém, o que queríamos era alterar valores da tupla, não da lista. Então, sabendo que podemos SOBRESCREVER a atribuição de uma tupla, é isso que faremos.

tupla = tuple(lista) #Sobrescreve a variável tupla transformando em tipo 'tuple' os valores da lista.
print(tupla)
