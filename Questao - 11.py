tipo = input("Abasteceu com alcoool ou gasolina? ")
if tipo == 'gasolina':
    print("O preço final da gasolina é: 6.50")
elif tipo == 'alcool':
    desconto = 5.00 * 0.95
    print(f"O preço final do alcool é: {desconto:.2f}")
else:
    print("Combustivel invalido")