"""

Estruturas de repetição

while
for
do while

"""
#Utilizando 3 parâmetros no for temos que:
#O primeiro parâmetro define onde iniciar o loop
#O segundo parâmetro define a posição final do loop
#O terceiro parâmetro define a cada quantas repetições o código
#será executado, ou seja será executado em 2 e em 2+5.

for x in range(2, 10, 5):
    print(x)

#Neste caso, se iniciará em 0, irá até a posição nº6 e 
#executará a cada 1 repetição
for x in range(0, 6, 1): #o mesmo resultado que range(6)
    print(x)