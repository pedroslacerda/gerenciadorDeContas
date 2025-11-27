contas = []

while True:
    print("\n---MENU PRINCIPAL---")
    print("1. Adicionar conta")
    print("2. Listar contas")
    print("3. Marcar conta como paga")
    print("4. Calcular total do mês")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":

        print("\nVocê escolheu a função de adicionar conta!")
        nome = (input("Digite o nome da conta que deseja adicionar: "))
        valor = float (input("Digite o valor da conta adicionada: "))
        vencimento = int (input("Digite o dia do vencimento da conta: "))

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

        if len(contas) == 0:
            print("Não há contas cadastradas!")

        else:
            print("\nLista de contas:")
            for conta in contas:
                status = "PAGA" if conta ["paga"] else "NÃO PAGA"

                print(f"{conta['nome']} - R${conta['valor']} - Vence dia {conta['vencimento']} - {status}")

    elif escolha == "3":
        print("Você escolheu a função de marcar conta como paga!")

        if len(contas) == 0:
            print("Não há contas cadastradas!")
        else:
            print("\nContas disponíveis: ")

            for i, conta in enumerate (contas):
                status = "PAGA" if conta ["paga"] else "NÃO PAGA"
                print(f"{i + 1}. {conta['nome']} - R${conta['valor']} - {status}")

            escolha = int(input("Digite o número da conta que deseja marcar como pago: "))

            indice = escolha - 1

            if 0 <= indice < len(contas):
                contas[indice]["paga"] = True
                print(f"\n***A conta '{contas[indice]['nome']}' foi marcada como PAGA***")

            else:
                print("Opção inválida!")

    elif escolha == "4":
        print("Você escolheu a função de calcular total do mês!")

        if len(contas) == 0:
            print("Não há contas cadastradas!")

        else:
            total = 0
            for conta in contas:
                total += conta ["valor"]
            print(f"\n***O total de contas do mês é: R$ {total:.2f}***")

    elif escolha == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida, tente novamente.")
