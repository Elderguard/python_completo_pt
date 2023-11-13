def par_impar():
    #Se apenas salvarmos e executarmos o código, o programa entenderá que o corpo da função está vazio, gerando um erro.
    #Caso seja interessante ignorar esse erro para fins de testar o restante do código, podemos utilizar o comando pass.
    pass

par_impar()

#A utilização de funções vazias pode criar vulnerabilidades e problemas de segurança. Então por que utilizar?

var = 0
if var == 0:
    # aqui neste exemplo existem códigos abaixo do ponto em que o programa apresenta o erro, como o programa executa tudo de forma sequencial, se houverem erros nas instruções seguintes, não será percebido enquanto está apontando que esse trecho está vazio. Por isso, o pass é utilizado como uma forma temporária de ignorar este erro para encontrar possíveis erros após este trecho.
    pass 

print("ola mundo")
print(var)