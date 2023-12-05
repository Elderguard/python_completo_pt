# RECURSÃO

# Definição circular. É quase como um loop infinito.

# Sem recursão como funcionaria?
def fatorialS(numero):
    fatorial = 1
    if numero == 0:
        return 1
    else:
        for x in range (1, numero +1):
            fatorial *= x
        return fatorial
    

print(fatorialS(5))

# Com recursão:
def fatorialR(numero):
    if numero == 0:   # Critério de parada
        return 1
    else:
        # Parâmetro da chamada recursiva
        return numero * fatorialR(numero - 1)
#Os dois itens comentados acima são de extrema importância ao usar a recursividade.

print(fatorialS(5))