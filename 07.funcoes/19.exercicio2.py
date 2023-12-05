### DEFINIÇÕES DE VARIÁVEIS ###

valores = []

### FUNÇÕES ###

def bem_vindo():
    print("Olá, bem-vindo! Este programa tem por objetivo receber dois valores inteiros e executar uma operação de potenciação.")


def coletar_valores():
    valores.append(int(input('Digite o valor base da exponenciação: ')))
    valores.append(int(input('Digite o valor expoente da exponenciação: ')))


def calcular_potenciacao():
    potenciacao = valores[0]**valores[1]
    print(potenciacao)


### PROGRAMA PRINCIPAL ###
bem_vindo()
coletar_valores()
calcular_potenciacao()