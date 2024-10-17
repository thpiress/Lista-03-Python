idade = int(input("Digite a idade: "))
if idade < 18:
    print("Usuario menor de idade")
elif idade > 17 and idade <= 60:
    print("Usuario Adulto")
else:
    print("Usuario idoso")