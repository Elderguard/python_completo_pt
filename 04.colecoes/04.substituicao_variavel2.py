#Vimos anteriormente que é possível substituir os valores de variáveis utilizando uma variável temporária. Porém é possível realizar essa substituição em python sem precisar da variável temporária.

x = 5
y = 0

print(f"O valor de x é {x} e o valor de y é {y}")

x, y = y, x

print(f"O valor de x é {x} e o valor de y é {y}")