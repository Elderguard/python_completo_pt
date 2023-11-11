"""
do while

Código para adivinhar um número

"""

palpite = 0
numero = 9

while palpite != numero:
    print("Adivinhe qual o número correto. Qual o seu palpite? \n")
    palpite = int(input())

print("Parabéns você acertou!")
#print("Você errou!")
