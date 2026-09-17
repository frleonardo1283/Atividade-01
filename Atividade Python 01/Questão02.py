import os
os.system("cls || clear")

nome = input("Digite o seu nome: ")
genero = input("Digite o seu gênero (M/F): ")
estado_civil = input("Digite o seu estado civil (S/C/D/V): ")
os.system("cls || clear")

match genero:
    case "M" | "m":
        print("Gênero: Masculino")

        match estado_civil:
            case "S" | "s":
                print(f"Olá {nome}, você é do gênero masculino e está solteiro.")

            case "C" | "c":
                print("Estado civil: Casado")
                tempo_casamento = int(
                    input("Digite o tempo de casamento em anos: ")
                )

                print(
                    f"Olá {nome}, você é do gênero masculino "
                    f"e está casado há {tempo_casamento} anos."
                )

            case "D" | "d":
                print(f"Olá {nome}, você é do gênero masculino e está divorciado.")

            case "V" | "v":
                print(f"Olá {nome}, você é do gênero masculino e está viúvo.")

            case _:
                print("Estado civil não identificado.")

match genero:
    case "F" | "f":
        print("Gênero: Feminino")

        match estado_civil:
            case "S" | "s":
                print(f"Olá {nome}, você é do gênero feminino e está solteira.")

            case "C" | "c":
                print("Estado civil: Casada")
                tempo_casamento = int(
                    input("Digite o tempo de casamento em anos: ")
                )

                print(
                    f"Olá {nome}, você é do gênero feminino "
                    f"e está casada há {tempo_casamento} anos."
                )

            case "D" | "d":
                print(f"Olá {nome}, você é do gênero feminino e está divorciada.")

            case "V" | "v":
                print(f"Olá {nome}, você é do gênero feminino e está viúva.")

            case _:
                print("Estado civil não identificado.")

if genero not in ("M", "m", "F", "f"):
    print("Gênero não identificado.")