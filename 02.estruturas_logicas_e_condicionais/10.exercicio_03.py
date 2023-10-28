print("Este programa calcula o valor final do produto aplicando porcentagem de desconto")

preco = float(input("Qual é o preço do produto? "))
desconto = float(input("Qual é a porcentagem de desconto aplicado ao produto? "))

valor_final = preco - preco*desconto/100
print(f"O valor do produto com desconto é R${valor_final}")
