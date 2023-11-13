####Criar um jogo de pedra, papel, tesoura!####

# IMPORT DE BIBLIOTECAS #

# Para criar esse jogo, vamos importar uma função de uma biblioteca chamada random.

# import random seria a forma de importar a biblioteca, porém se importarmos a biblioteca inteira, o jogo ficaria mais pesado do que o necessário. Portanto, usaremos outro método para importar apenas o que queremos utilizar:

from random import choice


# DEFINIÇÃO DE VARIÁVEIS GLOBAIS #
jogador_vitorias = 0
maq_vitorias = 0


# FUNÇÕES #
def opcao_jogador():
    escolha_do_jogador = input("Escolha Pedra, Papel ou Tesoura: ")
    escolha_do_jogador.lower() # Colocará o texto em minúsculo para não termos que criar uma lista com todas as opções.
    if escolha_do_jogador == 'pedra':
        return escolha_do_jogador
    elif escolha_do_jogador == 'papel':
        return escolha_do_jogador
    elif escolha_do_jogador == 'tesoura':
        return escolha_do_jogador
    else:
        print("Opção inválida. Tente novamente.")
        opcao_jogador() #Chamará a função de novo para retornar ao início da mesma.

def opcao_maquina():
    escolha_maquina = choice(['pedra', 'papel', 'tesoura']) 
    # Criará uma escolha aleatória de um dos elementos da lista
    return escolha_maquina


# PROGRAMA PRINCIPAL #
while True:

    print(30*"-")
    
    escolha_do_jogador = opcao_jogador() # Por se tratar de paradigma imperativo, sequencial, a reutilização do código nas instruções abaixo não entrarão em conflito com esta variável.
    
    escolha_maquina = opcao_maquina()

    print(30*"-")


    if(escolha_do_jogador == 'pedra') and (escolha_maquina == 'tesoura') \
        or (escolha_do_jogador == 'papel') and (escolha_maquina == 'pedra') \
            or (escolha_do_jogador == 'tesoura') and (escolha_maquina == 'papel'):
            #Jogador ganha
            print(f"Jogador escolheu {escolha_do_jogador} e a máquina escolheu {escolha_maquina}."
            " Resultado: Você Ganhou!")
            jogador_vitorias += 1 #adiciona 1 à variável
    elif escolha_do_jogador == escolha_maquina:
        #Empate
        print(f"Jogador escolheu {escolha_do_jogador} e a máquina escolheu {escolha_maquina}."
        " Resultado: Empate!")
    else:
        #Máquina ganha
        print(f"Jogador escolheu {escolha_do_jogador} e a máquina escolheu {escolha_maquina}."
        " Resultado: Você Perdeu!")
        maq_vitorias += 1


    print(30*"-")
    print(f"Vitórias do jogador: {jogador_vitorias}")
    print(f"Vitórias da máquina: {maq_vitorias}")
    print(30*"-")


    print(30*"-")
    escolha_do_jogador = input("Você quer jogar novamente? ")
    if escolha_do_jogador in ["SIM", "sim", "Sim", "s", "S"]:
        pass
    elif escolha_do_jogador in ['NAO', 'nao' "Nao",'NÃO', 'não', 'Não', 'n', 'N',]:
        print("Você escolheu sair.")
        break
    else:
        print("A informação digitada não corresponde aos parâmetros esperados, saindo do jogo.")
        break