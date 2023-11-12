#Se tentarmos criar uma tupla com um único elemento, teremos um problema na criação do seu tipo.
tupla = ('item1')
print(type(tupla))
#O resultado aqui é a mesma coisa de não existirem os parênteses()

#Então para criar uma tupla com um único elemento, de forma que o programa entenda como uma tupla, é necessário adicionarmos algo para indicar que trata-se de uma tupla.

tupla = ('item1',) #A vírgula faz com que o algoritmo entenda que trata-se de um tipo de listagem, uma tupla.
print(type(tupla))

del tupla

#Na realidade, o que faz com que uma tupla seja uma tupla não são os parênteses, são as vírgulas. Portanto, podemos criá-las sem os parênteses.

tupla = 'item1', #A vírgula faz com que o algoritmo entenda que trata-se de um tipo de listagem, uma tupla.
print(type(tupla))

del tupla

tupla = 'item1', 'item 2', 'item3', 'item4' #A vírgula faz com que o algoritmo entenda que trata-se de um tipo de listagem, uma tupla.
print(type(tupla))
