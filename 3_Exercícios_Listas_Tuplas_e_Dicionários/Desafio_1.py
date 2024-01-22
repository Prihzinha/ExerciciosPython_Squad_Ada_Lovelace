Lista_resp = []

resp1 = input("Telefonou para a vítima? (S/N): ")
Lista_resp.append (resp1)
resp1 = input("Esteve no local do crime? (S/N): ")
Lista_resp.append (resp1)
resp1 = input("Mora perto da vítima? (S/N): ")
Lista_resp.append (resp1)
resp1 = input("Devia para a vítima? (S/N): ")
Lista_resp.append (resp1)
resp1 = input("Já trabalhou com a vítima? (S/N): ")
Lista_resp.append (resp1)

qtd_sim = 0
for i in range(len(Lista_resp)):
    if Lista_resp[i].upper() == "S":
        qtd_sim += 1

if qtd_sim == 5:
    print("Assasino!")
elif qtd_sim > 3:
    print("Cúmplice")
elif qtd_sim > 1:
    print("Suspeita")
else:
    print ("inocente")

#print(Lista_resp)