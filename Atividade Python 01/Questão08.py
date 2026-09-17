import os 
os.system("cls || clear")

cor=input("""Digite o numero correspondente a cor: 
           1 para Verde
           2 para Azul
           3 para Amarelo
           4 para Vermelho
          
""")
os.system("cls || clear")

match cor:
    case "1":
        print("Verde=R$ 10,00")
    case "2":
        print("Azul=R$ 20,00")
    case "3":
        print("Amarelo=R$ 30,00")
    case "4":
        print("Vermelho=R $40,00")
    case _:
        print("Cor inválida")

print(f"Cor: {cor}")
