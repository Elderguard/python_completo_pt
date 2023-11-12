# DICIONÁRIOS OU MAPAS

"""
Listas são coleções ordenadas, mutáveis que permitem valores duplicados
Tuplas são coleções ordenadas, imutáveis que permitem valores duplicados
Dicionários são coleções não-ordenadas, mutáveis que não permitem valores duplicados

"""
#index      0        1        2    ---ordenável
lista = ['item1', 'item2', 'item3']
tupla = ('item1', 'item2', 'item3')

#não-ordenável, sistema chave:valor
dicio = {"chave1": "Gabriel", "chave2": "1993", "chave3" : True}
print(dicio)

# Também é possível declarar o dicionário sem estar em linha, como um bloco.
dicionario = {
    "nome":"Bruna",
    "idade": 27,
    "nacionalidade": "brasileira"
}
print(dicionario) # A representação no console não muda independentemente do formato usado para declarar.

#se na variavel dicionario tentarmos adicionar outra chave com um dos nomes já utilizados, por exemplo 'idade', o programa sobrescreveria a informação duplicada.
dicionario = {
    "nome":"Bruna",
    "idade": 27,
    "nacionalidade": "brasileira",
    "idade": 35
}
print(dicionario)

#Imprimindo elementos isolados
print(lista[0]) # Podemos imprimir da lista usando o índice
print(tupla[0]) # Podemos imprimir da tupla usando o índice

print(dicionario["nome"]) # Para imprimir do dicionário, temos que informar a chave que queremos imprimir

#Outra forma de acessar esses elementos é por meio da função get
print(dicionario.get("nome"))

"""
Executando o python para analisar as propriedades de dicionarios, encontramos os comandos e atributos dos mesmos.

>>> dicio = {'idade':23}
>>> dir(dicio)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

"""

print(dicionario.keys()) # Imprimirá apenas o nome das chaves no dicionário.

print(len(dicionario)) # Imprimirá a quantidade de elementos no dicionário.

print(dicionario.values()) # Imprimirá apenas os elementos no dicionário.

if 'idade' in dicionario: # Se houver idade em dicionário, executará o código.
    print("A chave idade existe")

print(dicionario.items()) # Mostrará todos os itens dentro de dicionário, tendo tuplas dentro da lista.