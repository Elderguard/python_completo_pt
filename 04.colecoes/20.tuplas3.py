
#vamos supor que criamos uma lista com estados do brasil, porém o usuário tem a possibilidade de alterar a lista, adicionando novos items. Isso possibilita a inserção de itens que não correspondem à realidade, poluindo nossa lista.
unidadesFederativasBrasil = ['SP', 'DF', 'GO', 'SS']
print(type(unidadesFederativasBrasil))

del unidadesFederativasBrasil
#Para evitar este tipo de problema, é utilizada a tupla.
unidadesFederativasBrasil = ('SP', 'DF', 'GO')
print(type(unidadesFederativasBrasil))
