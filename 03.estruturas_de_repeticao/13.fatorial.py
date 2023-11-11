"""
Como achar o fatorial de um número

4! = 4*3*2*1

9! = 9*8*7*6*5*4*3*2*1
"""

numero = int(input("Insira um numero: "))

fatorial = 1

if numero < 0:
    print("Não existe fatorial de números negativos")
elif numero == 0:
    print("O fatorial de {numero} é 1")
else:
    for x in range(1, numero+1):
        fatorial = fatorial*x
        #fatorial = 1*1+1*2+...+1*n
print (f"O fatorial de {numero} é {fatorial}.")
