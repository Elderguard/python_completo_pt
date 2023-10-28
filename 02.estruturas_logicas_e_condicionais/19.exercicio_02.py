print("Este programa tem por objetivo classificar um nadador de acordo com sua idade.")

idade = int(input("Qual a idade do nadador? "))

if 5<=idade<=7:
    print("Infantil A")
elif 7<idade<=10:
    print("Infantil B")
elif 10<idade<=13:
    print("Juvenil A")
elif 13<idade<=17:
    print("Juvenil B")
else:
    print("A idade digitada não pertence a nenhuma das categorias.")
