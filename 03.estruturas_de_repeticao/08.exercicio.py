"""
Exercício - Trocar variáveis
"""

# Trocando variaveis em python

x = input("Insira o valor de x: ")
y = input("Insira o valor de y: ")

print(f"O valor de x antes da troca é {x}")
print(f"O valor de y antes da troca é {y}")

# Criaremos uma variavel temporaria

temp = x   #A temporaria guardará o valor de x para que não 
# se perca este valor durante a troca

x = y    # O valor de x será sobrescrito com o valor de y
y = temp # O valor de y será sobrescrito com o valor na variavel 
         # temporaria

print(f"O valor de x depois da troca é {x}")
print(f"O valor de y depois da troca é {y}")