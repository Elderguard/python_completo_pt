def ola_mundo():
    print('ola mundo')


def executar(): 
    ola_mundo() #É possível ter uma função dentro de outra função. Ou uma função que chama múltiplas funções.


executar()
#porém, tome cuidado com isso. Se chamarmos a função ola_mundo dentro dela mesma, criamos um loop infinito. Com isso, podemos esgotar todos os recursos do computador e causar problemas ao computador, geralmente forçando um travamento da máquina.