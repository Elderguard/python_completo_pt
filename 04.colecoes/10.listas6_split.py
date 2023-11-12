#index      0        1        2 
lista = ["carro", "barco", "avião"]
print(lista)

#imprime os elementos separadamente
for x in lista:
    print(x)

#imprime o número de elementos da lista
print(len(lista))

#impressão dos índices da lista
for x in range(3):
    print(x)

#impressão do índice e do valor naquele índice
for x in range(len(lista)):
    print(f"No índice {x} se encontra o valor {lista[x]}")

#separar cada caractere e adicionar a um índex da lista
texto = "carro, avião"
lista2 = list(texto)
print(lista2)

#a função split separará as informações espaçadas
texto1 = texto.split()
print(texto1) #porém a vírgula será impressa junto.

#Para remover a vírgula, devemos indicá-la como parâmetro.
texto2 = texto.split(',')
print(texto2) #Agora neste caso, o espaço ' ' é que não foi removido. Isso ainda é possível de tratar com outros métodos.
#Neste caso simples, poderíamos simplesmente adicionar espaço após a vírgula no parâmetro.
texto3 = texto.split(', ')
print(texto3)
#Porém nem sempre há certeza de que haverá este exato padrão, então quando há incerteza deverão ser aplicados outros métodos.

#Essa é uma ferramenta útil por exemplo para separar informações em um endereço de e-mail.
texto4 = "meunome@gmail.com"
texto4 = texto4.split('@')
print(texto4)