lado1 = int(input("Digite o comprimento do primeiro lado: "))
lado2 = int(input("Digite o comprimento do segundo lado: "))
lado3 = int(input("Digite o comprimento do terceiro lado: "))

if lado1 == lado2 == lado3:
    print("O triângulo é EQUILÁTERO (todos os lados têm o mesmo comprimento).")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo é ISÓSCELES (dois lados têm o mesmo comprimento).")
else:
    print(
          "O triângulo é ESCALENO (todos os lados têm comprimentos distintos)."
        )
