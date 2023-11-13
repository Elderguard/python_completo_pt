# PARADIGMA IMPERATIVO

"""
O paradigma imperativo é a forma de programação tradicional, que existe antes de surgir a programação orientada a objeto.

imperare vem do latin "comandar" em que se traduz os algoritmos para a linguagem mais adequada para a máquina.

Características:
Variáveis, atribuições e sequência.

O algoritmo é um passo a passo para resolver um problema, de forma lógica e sequencial.
Portanto, o paradigma imperativo segue uma lógica mais natural de programação, tanto para o ser humano quanto para a máquina.

Exemplos de linguagens que utilizam esse paradigma:
C, Fortran, Cobol, Basic, Pascal, Ada, Modula-2
--------------------

É possível verificar que se tivermos uma mesma variável em arquivos diferentes de código, com valores diferentes. Uma não irá interferir na outra seguindo os procedimentos dos códigos desenvolvidos até este momento. Cada arquivo forma sua propria limitação, ou escopo.
--------------------
É possível que dentro de um único arquivo, tenhamos a intenção de criar mais do que uma variável com o mesmo nome, ou que não são acessíveis em qualquer parte do programa.
-------------------
Os códigos desenvolvidos até aqui utilizam apenas blocos externos, ou seja, produz variáveis globais, por isso as variáveis podem ser acessadas em qualquer parte do programa, naquele arquivo.

Porém, é possível criar variáveis em blocos internos, que não serão acessíveis em qualquer lugar do código. Estas variáveis são chamadas variáveis locais.

Uma função é um bloco de código que pode ser criado e nomeado e chamado para execução em qualquer momento do programa, com seus próprios comandos pré-definidos. Pode ser chamada a qualquer momento e quantas vezes for necessário.
"""
#bloco externo
nome = 'Gabriel' #variável global


def minha_funcao(): # Aqui estamos criando e definindo a função
    #bloco interno - conhecido como corpo da função
    nome = 'Ana' #variável local
    print(nome)
    tupla = 2,5,6,7,9
    print(tupla)
    if nome == 'Ana':
        print("Impressão do bloco interno da condição if")
    for x in tupla:
        print(x)
    #A função não é executada imediatamente ao ser criada, ela precisa ser chamada no bloco externo, no programa principal.


print(nome)
minha_funcao() # Somente aqui a função está sendo chamada, e será executada, se a função nunca for chamada, nunca será executada.