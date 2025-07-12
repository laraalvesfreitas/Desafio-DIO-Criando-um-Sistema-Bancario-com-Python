menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":   #Depósito
        valor = float(input("Por favor, informe o valor que deseja depositar "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Operação de depósito realizada com sucesso")

        else:
            print("Operação não realizada: valor informado inválido.")

    elif opcao == "s": #Saque
        valor = float(input("Por favor, informe o valor que deseja sacar: "))



        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        print("Operação de saque realizada com sucesso")


        if excedeu_saldo:
            print("Operação não realizada: Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação não realizada: O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação não realizada: Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1



        else:
            print("Operação não realizada: valor informado inválido.")

    elif opcao == "e": #Extrato
        print("\n================ EXTRATO ================")
        print("Não houve movimentações registradas" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q": #Sair
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")