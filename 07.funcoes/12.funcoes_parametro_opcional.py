#Parâmetro Opcional

def imprimir_nome(nome,sobrenome,idade):
    print('nome: ', nome)
    print('sobrenome: ', sobrenome)
    print('idade: ', idade)


"""

imprimir_nome() 

"""
#se tentarmos rodar o código com menos parâmetros do que a função necessita (exemplo acima), o código terá um TypeError pois faltarão argumentos.
#Além do parâmetro padrão visto anteriormente que determina um valor alternativo, outra forma de evitar isso é a definição de parâmetros padrões opcionais que determinarão o parâmetro como não obrigatório, 'nenhum'.

def imprimir_nome(nome=None,sobrenome=None,idade=None):
    print('nome: ', nome)
    print('sobrenome: ', sobrenome)
    print('idade: ', idade)


imprimir_nome()
print(30*"-")
imprimir_nome('maria','clara',35)
print(30*"-")
imprimir_nome('maria')

#Essa padronização permite aplicar condicionais dentro da função para execuções mais filtradas.

def imprimir_nome(nome=None,sobrenome=None,idade=None):
    if nome != None:
        print('nome: ', nome)
        print('sobrenome: ', sobrenome)
        print('idade: ', idade)
    else:
        print("Por favor, insira seus dados")

print(30*"-")
imprimir_nome()
print(30*"-")
imprimir_nome('maria','clara',35)
print(30*"-")
imprimir_nome('maria')