"""
Python - Comandos de controle condicional

if, else e elif (else if)

"""

print("Executando primeira condicional")
x = 3
y = 8

if y > x: 
    print("y é maior do que x")
elif y<x:
    print("y é menor do que x")
elif y==x:
    print("x é igual a y")

print("Código fora do bloco condicional")
print(y>x)
print(y<x)
print(y==x)

print("Executando segunda condicional")
x = 3
y = 3

if y > x: 
    print("y é maior do que x")
elif y<x:
    print("y é menor do que x")
else: #pode ser usado o else neste caso ao invés de condicionar novamente
    print("x é igual a y")

print("Código fora do bloco condicional")
print(y>x)
print(y<x)
print(y==x)

print("Executando terceira condicional")
x = 3
y = 1

if y > x: 
    print("y é maior do que x")
elif y<x:
    print("y é menor do que x")
else:
    print("x é igual a y")

print("Código fora do bloco condicional")
print(y>x)
print(y<x)
print(y==x)
