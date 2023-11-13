def par_impar():
    numero = 4
    if (numero % 2) == 0: # Se o resto da divisão for igual a 0
        return "numero par"
    else:
        return "numero impar"


print(par_impar())

print(30*"-")

#####################
#O mesmo código da função pode ser escrito sem o else

def par_impar():
    numero = 5
    if (numero % 2) == 0: # Se o resto da divisão for igual a 0
        return "numero par"
    return "numero impar"


print(par_impar())

print(30*"-")

# Relembrando que numero é uma variável local existente apenas internamente no bloco da função par_impar, caso tentemos imprimir a variável no bloco do programa, o programa informará o erro 'numero' is not defined.


# No caso de uma condicional comum, se a condicional for satisfeita, a instrução será executada e a próxima fora da condicional também, como no código abaixo:
x = 0
if x == 0:
    print("0")
print("ola")

print(30*"-")

# Enquanto se a condicional não for satisfeita, a instrução dentro da condicional não será executada, passando à próxima instrução do programa.
x = 1
if x == 0:
    print("0")
print("ola")

print(30*"-")

# Porém, como foi observado acima com o return, o comportamento foi diferente.
# E se usarmos o print ao invés do return?
def par_impar():
    numero = 4
    if (numero % 2) == 0: # Se o resto da divisão for igual a 0
        print("numero par")
    print("numero impar")


par_impar() #As duas impressões serão executadas.

print(30*"-")

### Por que o mesmo não acontece com o return?
# A palavra return está dando um comando de sair da função. Por isso, ao ler e executar o primeiro 'return', o programa imediatamente sai da função, ignorando o restante do código interno da função. Por isso, a função abaixo funciona.

def par_impar():
    numero = 4
    if (numero % 2) == 0: # Se o resto da divisão for igual a 0
        return "numero par"
    return "numero impar"


print(par_impar())

print(30*"-")