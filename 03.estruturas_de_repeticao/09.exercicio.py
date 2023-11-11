"""
Exercício -Igual maior ou menor a zero
"""
numero = float(input("Digite um número: "))

if numero > 0:
    print(f"{numero} é maior que zero")
elif numero == 0:
    print(f"{numero} é igual a zero")
else:
    print(f"{numero} é menor do que zero")