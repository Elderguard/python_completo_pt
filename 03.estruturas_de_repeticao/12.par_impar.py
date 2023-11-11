"""
descobrir se um número é impar ou par

Número par é aquele que quando dividido por 2 tem resto 0.
0,2,4,6,8... 
"""
print(30 * "-")  # imprime 7 vezes o caracter -
numero = int(input("Insira um numero para saber se é par: "))
if (numero % 2) == 0:
    print(f"{numero} é um número par")
else:
    print(f"{numero} é um número ímpar")
print(30 * "-")  # imprime 7 vezes o caracter -