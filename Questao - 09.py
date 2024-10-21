salario = float(input("Digite o salario do usuario: "))

if salario < 1000:
    aumento = salario * 1.10
else:
    aumento = salario * 1.05

print(f"O salario com aumento ficou: R$ {aumento:.2f}.")