# DICIONÁRIOS OU MAPAS

# index      0        1        2    ---ordenável
lista = ['item1', 'item2', 'item3']
tupla = ('item1', 'item2', 'item3')

# chave:valor
dados = {'nome' : 'Gabriel', 'ano' : 1993, 'valorLogico' : True}
dados.update({'estado':'Rio de Janeiro'})
print(dados)

# dicio = dict.(tupla)
# O comando acima geraria o seguinte erro:
# ValueError: dictionary update sequence element #0 has length 5; 2 is required

#A forma adequada é:
dicio = dict.fromkeys(tupla)
print(dicio)
#O comando transforma as informações na tupla em chaves para o dicionário. Os elementos serão definidos como 'None', não tendo valor definido.

# Para passarmos valores:
x = 0 # Criamos uma variável x com valor 0
dicio = dict.fromkeys(tupla, x)
print(dicio)
#Nesse caso, os elementos terão valor definido como 0.

# E se decidirmos passar outra tupla:
tupla2 = ('valor1', 'valor2', 'valor3')
dicio = dict.fromkeys(tupla, tupla2)
print(dicio)
#Nesse caso, os elementos terão valor definido como 0.