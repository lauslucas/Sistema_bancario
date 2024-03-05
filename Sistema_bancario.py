# Sistema Bancário
menu = '''

[1] Deposito
[2] Saque
[3] Extrato
[4] Sair

='''

saldo = 0
limite = 1000
extrato = ""
numero_saques = 0
limite_saques_diario = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print(f"R$ {valor:.2f} depositado!")

        else:
            print("Operacão inválida! Tente novamente.")

    elif opcao == "2":
        valor = float(input("Informe o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_n_saque = numero_saques > limite_saques_diario

        if excedeu_saldo:
            print("Operacão falhou! Sem saldo o suficiente")

        elif excedeu_limite:
            print("Operacão falhou! Excedeu o limite de saque.")

        elif excedeu_n_saque:
            print("Operacão falhou! Excedeu o número de saques diário.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque no valor de R$ {valor:.2f} realizado.")

        else:
            print("Operacão falhou! Informe um valor válido.")

    elif opcao == "3":
        valor = saldo
        print("\n>>>>> EXTRATO <<<<<")
        print("Não foi realizada movimentacões." if not extrato else extrato)
        print(f"\n Saldo: R$ {valor:.2f}")

    elif opcao == "4":
        print("Volte sempre!")
        break

    else:
        print("Operacão inválida! Tente novamente.")
