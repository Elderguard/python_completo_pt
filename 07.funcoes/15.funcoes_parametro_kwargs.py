#Argumento Arbitrário *args

#Neste exemplo, será utilizado um número de argumentos maior do que o número de parâmetros.

# 3 parâmetros + *args
def imprimir_imovel(nome_imovel,n_quartos,vagas_garagem=None, *args):
    print(30*"-")
    print('Título: ', nome_imovel)
    print('Quartos: ', n_quartos)
    if vagas_garagem != None: 
        #somente executará se for definido o terceiro parâmetro
        print('Vagas na garagem: ', vagas_garagem)
        

#               4 argumentos
imprimir_imovel("Loja Comercial", 2, 5, 'desconto') 
#Nesse exemplo, os argumentos excedentes serão atribuídos *args, que não será impresso pois não há tal solicitação.

# E se criarmos uma função apenas com argumentos arbitrários?

def imprimir_nomes(*nomes):
    print(30*"-")
    print(nomes)


imprimir_nomes('ana','beatriz', 'pedro', 'joão')
#Note que a impressão do resultado deste código demonstra que foi criada uma TUPLA com os valores informados como argumentos.

#Ou seja, o argumento arbitrário funciona como uma tupla.

#O que acontece se criarmos uma lista e usarmos a lista como parâmetro?

lista = ['ana', 'beatriz', 'pedro', 'joão']
imprimir_nomes(lista)
#Note que a impressão mostra que a lista inteira foi incluída dentro do primeiro item da TUPLA.

#E se quisermos distribuir essa lista na tupla?
#basta adicionar o asterístico antes do nome da lista.
#Isso fará o DESEMPACOTAMENTO da lista.
imprimir_nomes(*lista) 