nota = float(input("Digite a nota do aluno: "))
if nota >= 7:
    print("Aluno Aprovado")
elif nota > 4 and nota < 7:
    print("Aluno em recuperação")
else:
    print("Aluno reprovado")