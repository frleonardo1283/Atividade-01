import os
os.system("cls || clear")

valor_A=int(input("Digite o valor de A: "))
valor_B=int(input("Digite o valor de B: "))
valor_C: int
os.system("cls || clear")

if valor_A == valor_B:
    valor_C = valor_A + valor_B
    print(f"O valor de A{valor_A} e B{valor_B} são iguais, então serão somados ")
else:
    valor_C = valor_A * valor_B
    print(f"O valor de A{valor_A} e B{valor_B} são diferentes, então serão multiplicados")

print(f"Valor de C: {valor_C}")