"""
Como descobrir se um número é primo

O número deve ser divisível por 2 números (1 e ele mesmo) 
"""
print(30 * "-")
numero = int(input("Insira um numero para descobrir se é primo: "))

if numero > 1:
    for x in range (2, numero):
        if(numero % x) == 0:
            print(f"{numero} não é um número primo")
            break
    else:
        print(f"{numero} é um número primo")
else:
    print("Esse número não é primo: número menor ou igual a 1")

print(30 * "-")