#Parâmetro Opcional

#Neste exemplo, vamos definir os 2 primeiros argumentos como obrigatórios e o 3° será opcional.
def imprimir_imovel(nome_imovel,n_quartos,vagas_garagem=None):
    print('Título: ', nome_imovel)
    print('Quartos: ', n_quartos)
    if vagas_garagem != None: 
        #somente executará se for definido o terceiro parâmetro
        print('Vagas na garagem: ', vagas_garagem)
        


print(30*"-")
imprimir_imovel("Casa 3 Quartos - SP", 3)

#Observação: na definição dos parâmetros da função, deve-se primeir informar os parâmetros obrigatórios e depois os não obrigatórios. Caso isso não seja obedecido, o programa retornará um erro de sintaxe.
'''SyntaxError: non-default argument follows default argument'''