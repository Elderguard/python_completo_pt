# Funções são usadas principalmente para estruturação de programas e reutilização de códigos.
# Um programa é construído de blocos de código com tarefas específicas e bem definidas.
# A reutilização é para evitar repetir o mesmo código diversas vezes, simplificando a escrita e reduzindo o tamanho do código final do programa.

# O retorno da função é uma forma de devolver um valor que foi trabalhado internamente na função de volta para o programa principal. Nem toda função precisa ter retorno, porém é uma propriedade de grande utilidade.

lista = [1,2,3,4,5]
print(lista)

#Utilizamos a função pop diversas vezes até agora, mas qual é o retorno desta função? Devemos atribuir a uma variável para ver esse retorno.

retorno = lista.pop() # Atribui à variável 'retorno' o retorno do comando pop
print(lista) # Imprimirá a lista após comando pop, removendo o último elemento
print(f"O retorno da função pop é: {retorno}") # Imprimirá o valor guardado na variavel retorno, que é o elemento removido da lista com o comando pop.

### Sendo assim, qual o retorno da função print()?

retorno = print("Ola mundo")
print(f"O retorno da função pop é: {retorno}") # Imprimirá o valor guardado na variavel retorno - None. Ou seja, a função print não possui retorno.
