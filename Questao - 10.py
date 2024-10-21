preco = float(input("Digite o valor do produto: "))
if preco > 100:
    desconto = preco * 0.90
    print(f"O valor com desconto é de: R$ {desconto:.2f}")
else:
    print("Nao a desconto disponivel para este valor! ")