num1 = int(input("Digite o 1º numero: "))
num2 = int(input("Digite o 2º numero: "))
operador = input("Digite um operador:(+, -, *, /) ")
if operador == '+':
    result = num1 + num2
    print(f"O resultado da soma é: {result}")
elif operador == '-':
    result = num1 - num2
    print(f"O resultado da subtração é: {result}")
elif operador == '*':
    result = num1 * num2
    print(f"O resultado da multiplicação é: {result}")
elif operador == '/':
    result = num1 / num2
    print(f"O resultado da divisão é: {result:.1f}")
else:
    print("Operador Invalido!")