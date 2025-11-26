while True:
    print("MENU PRINCIPAL")
    print("1. Adicionar conta")
    print("2. Listar contas")
    print("3. Marcar conta como paga")
    print("4. Calcular total do mês")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":

        contas = []

        print("\nVocê escolheu a função de adicionar conta!")
        nome = (input("Digite o nome da conta que deseja adicionar: "))
        valor = float (input("Digite o valor da conta adicionada: "))
        vencimento = int (input("Digite o dia do vencimento da conta:"))

        conta = {
            "nome": nome,
            "valor": valor,
            "vencimento": vencimento,
            "paga": False #Quando adicionar ainda n foi paga
        }

        contas.append(conta)

        print(f"Conta '{nome}' adicionado com sucesso!\n")

    elif escolha == "2":
        print("Você escolheu a função de listar contas!")

        

    elif escolha == "3":
        print("Você escolheu a função de marcar conta como paga!")
    elif escolha == "4":
        print("Você escolheu a função de calcular total do mês!")
    elif escolha == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida, tente novamente.")
