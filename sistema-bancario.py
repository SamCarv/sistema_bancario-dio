saldo = 0
saque_max = 500
limite = 3
extrato = """"""


def menu():
    print("Menu")
    print("[d] Depositar")
    print("[s] Sacar")
    print("[e] Extrato")
    print("[q] Sair")


def estrato():
    print("Extrato")


while True:
    menu()

    opcao = input("=> ")

    if opcao == "d":
        print("Deposito")
        quantidade = float(input("Valor: "))
        print("Deposito realizado com sucesso!")
        saldo += quantidade
        extrato += f"Deposito de {quantidade:.2f}\n"
    elif opcao == "s":
        print("Sacar")
        saque = float(input("Valor: "))
        if limite > 0 and saque <= saque_max:
            saldo -= saque
            limite -= 1
            extrato += f"Saque de {saque:.2f}\n"
            print("Saque realizado com sucesso!")
        else:
            print(
                "Não foi possivel realizar o saque por falta de saldo ou limite de saques diários"
            )

    elif opcao == "e":
        print("Extrato")
        print(extrato)
        print(f"Saldo atual: {saldo:.2f}")
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada. ")
