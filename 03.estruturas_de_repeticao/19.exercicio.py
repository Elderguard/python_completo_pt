"""
Atribuição

Todos os exercícios possuem alguma repetição de lógica de forma que você pode utilizar laços de repetição para desenvolvê-los.
----------
02 - Escreva um programa para calcular as somas:

"""
#Mensagem de explicação do programa
print("Este programa tem por objetivo calcular a soma de valores informados pelo usuário")

#coletar valores e somar
soma = 0
while True:
    print (f"Soma: {soma}")
    entrada = input("Digite o valor a somar ou digite s para sair: ")
    if type(entrada) == str:
        if entrada == "s":
            print(f"Você desejou encerrar. \nO resultado da soma foi de {soma}")
            break
        else:
            num = float(entrada)
            soma = soma + num
