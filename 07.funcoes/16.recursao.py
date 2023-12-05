# RECURSÃO

# Definição circular. É quase como um loop infinito.

def reduzirNumero(numeroInt):
    while numeroInt > 0:
        print(numeroInt)
        numeroInt -= 1

reduzirNumero(5)
print(30*"-")
"""
1 - checar se o nosso número não é igual a 0
2 - se ele não for igual a 0, reduzir 1 unidade

5 (N - 1)
    4 (5 - 1)
        3 (4 - 1)
            2 (3 - 1)
                1 (2 - 1)
                    0 (1 - 1)
"""

def reduzirNumeroRecursao(numeroInt):
    print(numeroInt)
    if numeroInt>0:
        # N - 1
        reduzirNumeroRecursao(numeroInt - 1)

reduzirNumeroRecursao(5)