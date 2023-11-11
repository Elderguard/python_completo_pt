"""
Atribuição

Todos os exercícios possuem alguma repetição de lógica de forma que você pode utilizar laços de repetição para desenvolvê-los.
----------
01 - Escreva um programa que leia 5 valores e encontre o maior e o menor deles. mostre o resultado.

"""
#Mensagem de explicação do programa
print("Este programa tem por objetivo encontrar o menor e o maior valor entre números informados pelo usuário")

#coletar valores
num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
num3 = float(input("Digite o terceiro valor: "))
num4 = float(input("Digite o quarto valor: "))
num5 = float(input("Digite o quinto valor: "))

#comparações de maior
maior = num1

if maior<num2:
    maior = num2
if maior<num3:
    maior = num3
if maior<num4:
    maior = num4
if maior<num5:
    maior = num5

print(f"O maior valor dentre os informados é {maior}")

#comparações de menor
menor = num1

if menor>num2:
    menor = num2
if menor>num3:
    menor = num3
if menor>num4:
    menor = num4
if menor>num5:
    menor = num5

print(f"O menor valor dentre os informados é {menor}")
