"""
Continue é usado em estruturas de repetição
pass é usado em situações condicionais

"""
for x in range(10):
    if x == 3:
        continue #quando x for igual a 3, passará direto ao próximo
    print(x)

print(30*"-")

for x in range(10):
    if x == 3:
        pass #não fará diferença
    print(x)

print(30*"-")

if x ==5:
    pass #se o loop if estivesse vazio, daria erro na execução
         #usando pass, isso será ignorado. Use com cuidado.