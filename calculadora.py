def calculadora():
    print("Bem-vindo à Calculadora de Operações Básicas!")
    print("Escolha uma operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    escolha = input("Digite o número da operação: ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == "1":
        print(f"Resultado: {num1} + {num2} = {num1 + num2}")
    elif escolha == "2":
        print(f"Resultado: {num1} - {num2} = {num1 - num2}")
    elif escolha == "3":
        print(f"Resultado: {num1} * {num2} = {num1 * num2}")
    elif escolha == "4":
        if num2 != 0:
            print(f"Resultado: {num1} / {num2} = {num1 / num2}")
        else:
            print("Erro: divisão por zero não é permitida.")
    else:
        print("Opção inválida. Tente novamente.")

calculadora()
