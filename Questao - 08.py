lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    #Classificando triangulo:
    if lado1 == lado2 == lado3:
        tipo = "Equilatero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo = "Isoceles"
    else:
        tipo = "Escaleno"
    print(f"OS lados formam um triangulo do tipo: {tipo}.")
else:
    print("As medidas nao formam um triangulo!")
