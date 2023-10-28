print("Este programa tem por objetivo calcular a area de um retangulo")

base = input("Qual o tamanho da base? ")
altura = input("Qual a altura? ")

"""Se o código for executado sem a complementação de tipo,
a execução irá falhar, pois o input captura string"""

area = float(base) * float(altura)

print(f"O seu retângulo possui área de {area} unidades de medida ao quadrado")
