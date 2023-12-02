#Parâmetro Padrão

def imprimir_nome(nome,sobrenome,idade):
    print('nome: ', nome)
    print('sobrenome: ', sobrenome)
    print('idade: ', idade)


"""

imprimir_nome() 

"""
#se tentarmos rodar o código com menos parâmetros do que a função necessita (exemplo acima), o código terá um TypeError pois faltarão argumentos.
#Uma forma de evitar isso é a definição de parâmetros padrão que servirão como alternativa ao argumento que deveria ser informado.

def imprimir_nome(nome='nome',sobrenome='sobrenome',idade='idade'):
    print('nome: ', nome)
    print('sobrenome: ', sobrenome)
    print('idade: ', idade)


imprimir_nome()
print(30*"-")
imprimir_nome('maria','clara',35)
print(30*"-")
imprimir_nome('maria')

