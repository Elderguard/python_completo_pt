### DEFINIÇÕES DE VARIÁVEIS ###

valores = []

### FUNÇÕES ###

def bem_vindo():
    print("Olá, bem-vindo! Este programa tem por objetivo receber dois valores numéricos e retornar o maior e a média entre eles.")


def coletar_valores():
    valores.append(float(input('Digite o valor n° 1: ')))
    valores.append(float(input('Digite o valor n° 2: ')))


def determinar_maior():
    maior = max(valores)
    print(maior)


def calcular_media():
    media = sum(valores)/len(valores)
    print(media)

### PROGRAMA PRINCIPAL ###
bem_vindo()
coletar_valores()
determinar_maior()
calcular_media()