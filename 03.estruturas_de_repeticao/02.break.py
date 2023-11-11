"""
Estruturas de repetição - loops

while
for
do while

"""

# E se quiser interromper a repetição?
a = 0

while a <= 5:
    print(a)
    if a == 3:
        break
    a = a + 1

print(f"Resultado final de a: {a}")
# Devido à interrupção no meio do loop, o resultado final é
# diferente do que se espera olhando apenas para a condição
# do loop.

a = 0

while a <= 5:
    print(a)
    a = a + 1
else:
    print(f"a não é menor ou igual a 5, o valor de a é: {a}")

# É possível combinar while com o else.
