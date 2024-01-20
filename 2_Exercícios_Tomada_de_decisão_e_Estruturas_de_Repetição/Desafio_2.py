turno = input(
    "Em qual turno você estuda? Digite M para Matutino, "
    "V para Vespertino ou N para Noturno: ")

turno = turno.upper()

if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido! Por favor, digite M, V ou N.")
