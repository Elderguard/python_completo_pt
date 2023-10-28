print('Esse programa tem por objetivo classificar alguém como "Menor", "Emancipado" ou "Maior" de acordo com a sua idade')

idade = int(input("Qual é a idade de quem deseja classificar?"))

if idade < 16:
    print("MENOR")
elif 16<=idade<18:
    print("EMANCIPADO")
else:
    print("MAIOR")
