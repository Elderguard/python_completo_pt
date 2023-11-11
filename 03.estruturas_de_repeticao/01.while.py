"""
Estruturas de repetição - loops

while
for
do while

"""

# A intenção é somar valores, permitindo que eu inicie com um
# valor e consiga ao longo do código chegar a outro

# Para isso, podemos pensar em ter duas variáveis, onde a vai
# representar nosso valor inicial e x receberá o valor de a
# e será modificado para chegar no valor que queremos.

print("código utilizando a e x para a contagem")

a = 0
x = 0

print(a)
print(x)

x = a + 1
print(x)

# No código, iniciamos com o valor 0 e ao final teremos que
# x receberá o valor 1. Porém esse código é muito ineficiente
# tendo que usar duas variáveis para fazer a contagem.
# Felizmente, o computador é capaz de fazer esse procedimento
# usando apenas uma variável, assim o código pode ser:

print("código utilizando apenas a para a contagem")

a = 0
print(a)

a = a + 1
print(a)

# Porém, se quisermos que esse comportamento se repita,
# teríamos que repetir as linhas de código várias vezes
# até alcançar o valor esperado. Ao invés disso, podemos
# utilizar os LOOPs ou laços de repetição:

print("código utilizando laço de repetição")

a = 0

while a <= 5:
    print(a)
    a = a + 1

print(f"Resultado final de a: {a}")

# Com esse código simples, fizemos com que a fosse de 0 a 6.
