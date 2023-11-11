"""
do while

Código para adivinhar um número

"""

palpite = 5
numero = 9

while True:
    print("Adivinhe qual o número correto. Qual o seu palpite? \n")
    palpite = int(input())
    if palpite == numero:
        print("Parabéns você acertou!")
        break
    else:
        print("Você errou!")
else: #código para erros na aplicação
    print("Erro na aplicação")
    print(bool(palpite))