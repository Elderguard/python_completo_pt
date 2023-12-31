conjunto = {4, 6, 8, 9, 1, 'item'}
print(6 in conjunto) #True 
print(11 in conjunto) #False 
print('item' in conjunto) #True 
print('item2' in conjunto) #False 

# Acessando os itens do meu set
"""
Criando e acessando as propriedades de um conjunto no terminal, temos acesso a suas propriedades.
Podemos ver algumas funções de manipulação como 'add', 'clear', 'copy', 'pop', 'remove', 'update', etc.

>>> conj = {2,4,7,8}
>>> dir(conj)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
"""

set1 = {'item1', 'item2', 'item3'}
print (set1)
set1.add("item5")
print (set1)
set1.add(8)
set1.add(True)
print (set1)
