lista = ['item1', 'item2', 'item3']
print(f"A lista é: {lista}")
print(f"O tamanho da lista é : {len(lista)}")
print(f"O tipo da lista é: {type(lista)}")
print(30*"-")

#Uma tupla é uma única variável que consegue armazenar múltiplos itens.

#index      0        1        2
tupla = ('item1', 'item2', 'item3') #O nome da variável é irrelevante
print(f"A tupla é: {tupla}")
print(f"O tamanho da tupla é : {len(tupla)}")
print(f"O tipo da tupla é: {type(tupla)}")
print(f"O elemento no índice 2 é: {tupla[2]}")
print(30*"-")

#A diferença entre uma tupla e uma lista é que uma tupla é IMUTÁVEL enquanto a lista é MUTÁVEL.
del tupla #Remove a variável tupla 
tupla = ('item1', 'item2', 'item3', 'item1', 'item1') 
#cria nova variável tupla
print(f"A tupla é: {tupla}")
print(f"O tamanho da tupla é : {len(tupla)}")
print(f"O tipo da tupla é: {type(tupla)}")
print(f"O elemento no índice 2 é: {tupla[2]}")

#É possível também fazer contagem de repetição de elementos em uma tupla.
print(f"O elemento 'item 1' se repete {tupla.count('item1')} vezes")

"""
Ao iniciar o python 3 no terminal, conseguimos fazer uma comparação entre tuplas e listas:

>>> tupla = ('item1', 'item2')
>>> dir (tupla)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

>>> lista = ['item1', 'item2'] 
>>> dir(lista)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

É possível verificar que os comandos existentes para listas e os comandos existentes para tuplas são diferentes. Por exemplo, a tupla não tem os comandos 'append', 'clear', 'copy', 'extend', 'insert', 'pop', 'remove', 'reverse' e 'sort'. Enquanto isso, a lista não tem os comandos 'count' e 'index'.

Se tentarmos usar um atributo append na tupla, recebemos o erro:
AttributeError: 'tuple' object has no attribute 'append'.
"""