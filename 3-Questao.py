media = 0
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Diigte a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 7:
    print("Aluno Aprovado")
elif media < 7 and media >= 5:
    print("Aluno em recuperação")
else:
    print("Aluno reprovado")