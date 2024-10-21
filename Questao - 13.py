peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / (altura * altura)
if imc < 18.5:
    print("Usuario com Magreza")
elif imc >= 18.5 and imc <= 24.9:
    print("Usuario com peso normal")
elif imc >= 25 and imc <= 29.9:
    print("Usuario com Sobrepeso")
else:
    print("Usuario com Obesidade")