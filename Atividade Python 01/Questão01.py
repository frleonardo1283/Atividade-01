import os
os.system("cls || clear")

valor_A=(input("Digite o valor de A: "))
valor_B=(input("Digite o valor de B: "))
valor_C=(input("Digite o valor de C: "))
os.system("cls || clear")

soma= valor_A + valor_B

if soma < valor_C:
    print(f"a soma de A({valor_A}) e B({valor_B}) é menor do que o valor C({valor_C})")
elif soma == valor_C:
    print("todos os numeros são iguais")
else: 
    print(f"a soma de A({valor_A}) e B({valor_B}) é maior que o valor C({valor_C})")
