import random

dicionario = ["terra", "agua", "maritaca"]
palavra = random.choice(dicionario)
pletra = []
chances = 6
ganhou = False

def fchance():
    for letra in palavra:
        if letra.lower() in pletra:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print(f"Você tem {chances} chances")
while True:

    fchance()
    
    tentativa = input("Escolha uma letra para adivinhar: ")
    
    pletra.append(tentativa.lower())
    
    if tentativa.lower() not in palavra.lower():
        chances -= 1
    ganhou = True
    
    for letra in palavra:
        if letra.lower() not in pletra:
            ganhou = False
    if chances == 0 or ganhou:
        break
if ganhou:
    print(f"Parabéns. A palavra era: {palavra}")
else:
    print(f"Xiii... A palavra era: {palavra}")