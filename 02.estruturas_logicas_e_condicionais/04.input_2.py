"""
Função input() - Função para receber dados do usuário

"""

nome = input("Qual é o seu nome? ")
idade = input("Qual a sua idade? ")

#usar format para impressão
print("Seu nome é: {0} e sua idade é {1}".format(nome, idade))

#usar f para impressão
print(f"Seu nome é: {nome} e sua idade é {idade}")