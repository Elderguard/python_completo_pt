"""

Estruturas de repetição

while
for
do while

"""

s = "pernambuco"

for x in s:
    print(x)

"""
A estrutura for em python é diferente das usuais em outras
linguagens. A situação:

for (x = 0; x < 5; x++){
    print(x)
}

é representada em python da seguinte forma:
"""
#passando apenas um parâmetro serão realizadas as repetições até o sexto número, contabilizando o zero.
for x in range(6):
    print(x)