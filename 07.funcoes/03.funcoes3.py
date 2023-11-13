# Testando o retorno de uma função criada:
def ola_mundo():
    print('ola mundo')

retorno = ola_mundo()
print(retorno) # Aqui verificamos que nada está sendo retornado.

print(30*"-")

# Porém, podemos adicionar um retorno à função:
def ola_mundo():
    print('ola mundo')
    return 0

retorno = ola_mundo()
print(retorno) # Aqui verificamos que o retorno é 0.

print(30*"-")

# Podemos retornar a string:
def ola_mundo():
    return 'ola mundo'

retorno = ola_mundo()
print(retorno) # Aqui verificamos que o retorno 'ola mundo'.

print(30*"-")

#Porém com a forma que foi definida a função acima, se apenas chamarmos a função, nada será dado na saída do terminal.
ola_mundo()

# Poderia ser utilizado o retorno como parâmetro de impressão:
print(ola_mundo())
print(30*"-")