### DEFINIÇÕES DE VARIÁVEIS ###

valores = []
operacoes = ['+', '-','X','/','^','R', '1/X','%']

### FUNÇÕES ###

def bem_vindo():
    print("Olá, bem-vindo! Este programa tem por objetivo ser uma calculadora básica, realizando operações com até dois valores.")


def coletar_valores():
    pedir_primeiro_valor()
    operador = coletar_operacao()
    if operador != 'inverso':
        pedir_segundo_valor()
    interpretar_operacao(operador)

def pedir_primeiro_valor():
    valores.append(float(input('Digite o primeiro valor, base da operação: ')))

def pedir_segundo_valor():
    valores.append(float(input(f'Digite o segundo valor que operará sobre o valor base: {valores[0]} {valores[1]} ')))



def coletar_operacao():
    valores.append(input(f'Informe a operação dentro os mostrados a seguir: {operacoes}'))
    if valores[1].upper() == operacoes[0]:
        operador = 'adição'
    if valores[1].upper() == operacoes[1]:
        operador = 'subtração'
    if valores[1].upper() == operacoes[2]:
        operador = 'multiplicação'
    if valores[1].upper() == operacoes[3]:
        operador = 'divisão'
    if valores[1].upper() == operacoes[4]:
        operador = 'potência'
    if valores[1].upper() == operacoes[5]:
        operador = 'raíz'
    if valores[1].upper() == operacoes[6]:
        operador = 'inverso'
    if valores[1].upper() == operacoes[7]:
        operador = 'resto'

    return operador

def interpretar_operacao(operador):
    if operador == 'adição':
        adicao = valores[0]+valores[2]
        print(adicao)
    if operador == 'subtração':
        subtracao = valores[0]-valores[2]
        print(subtracao)
    if operador == 'multiplicação':
        multiplicacao = valores[0]*valores[2]
        print(multiplicacao)
    if operador == 'divisão':
        divisao = valores[0]/valores[2]
        print(divisao)
    if operador == 'potência':
        potencia = valores[0]**valores[2]
        print(potencia)
    if operador == 'raíz':
        radicando = valores[0]
        transforma_indice = valores[2] ** (-1)
        raiz = radicando**transforma_indice
        print(raiz)
    if operador == 'inverso':
        inverso = valores[0]**(-1)
        print(inverso)
    if operador == 'resto':
        resto = valores[0]%valores[2]
        print(resto)
    
    
### PROGRAMA PRINCIPAL ###
bem_vindo()
coletar_valores()
# calcular_multiplicacao()
