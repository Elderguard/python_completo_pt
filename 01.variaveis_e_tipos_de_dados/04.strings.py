print("ola")
print('ola')

w = "Curso de Python3"
print(w)

"""comentario não fica ocupando espaço na memória em execução"""

a = """ola, este é o curso de python
espero que goste"""

print(a) #imprime exatamente como foi escrito

#Métodos das Strings

b = " Ola Mundo "
print (b)       #será impresso com os espaços antes e depois

print (b.strip()) #será impresso ignorando os espaços em branco anterior e posterior ao texto

c = "Ola Mundo"
print(c.lower()) #será impresso com todas as letras em minúsculo

d = "ola mundo"
print(d.upper()) #será impresso com todas as letras em maiúsculo

e = "Ola"
f = "Mundo"
g = e + " " + f
print(g)