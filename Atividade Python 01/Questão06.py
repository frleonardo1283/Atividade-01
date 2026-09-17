import os
os.system("cls || clear")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
soma=nota1+nota2
media=soma/2
os.system("cls || clear")

if media >= 6:
    print("PARABÉNS! VOCÊ FOI APROVADO")
elif media < 6 and media >= 4:
    print("Recuperação")
else:
    print("Reprovado")

print(f"A média do aluno é: {media}")