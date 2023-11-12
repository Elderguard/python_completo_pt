#É possível armazenar diversos valores em uma lista, separados por vírgula

lista = ["chicago", "queens", "salvador", "pernambuco"]
print(lista)

lista2 = [2, 3, 7, 8, 10]
print(lista2)

lista3 = [2.0, 3.5, 6.3]
print(lista3)

#É possível unir/somar duas listas;
lista2 = lista2 + lista3

nome = "Curso de Python"
valor = range(10) #atribui à variável valor um range(0,10)

print(nome)
print(valor) #imprimirá informando um range(0,10)

lista7 = list(range(10)) #criará uma lista com todos os elementos no range, de 0 a 9.
print(lista7) #imprimirá todos os elementos da lista.

lista8 = list("Curso de Python") #transforma a string em uma lista, separando os elementos.
print(lista8) #imprimirá a lista.

elemento = 8 #cria a variável elemento atribuindo valor 8.

if elemento in lista7: #checa se o valor de elemento está na lista7
    print("Este elemento está dentro da lista")

