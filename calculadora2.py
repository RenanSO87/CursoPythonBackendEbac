# 1.Definição das operações matemáticas usando funções anônimas (lambda)
operacoes = {
    "1": ("Soma", lambda a, b: a + b),
    "2": ("Subtração", lambda a, b: a - b),
    "3": ("Multiplicação", lambda a, b: a * b),
    "4": ("Divisão", lambda a, b: a / b if b != 0 else "Erro: Divisão por zero"),
}

# 2. Criando as opções do menu dinamicamente usando List Comprehension
menu_opcoes = [f"{chave} - {valor[0]}" for chave, valor in operacoes.items()]

print("=== Calculadora Simples ===")

while True:
    # 3. Solicitação dos númemeros com tratamento de exceções (try-except)
    while True:
        try:
            num1 = float(input("\nInsira o primeiro número: "))
            break
        except ValueError:
            print("Valor inválido! Por favor, digite apenas números. ")

    while True:
        try:
            num2 = float(input("Insira o segundo número: "))
            break
        except ValueError:
            print("Valor inválido! Por favor, digite apenas números. ")

    # 4. Exibição do menu e escolha da operação
    print("\nEscolha uma operação:")
    for opcao in menu_opcoes:
        print(opcao)

    escolha = input("Você escolheu (digite o número): ").strip()

    if escolha not in operacoes:
        print("Operação inválida! Por favor, escolha uma opção válida.")
        continue

    nome_operacao, funcao_operacao = operacoes[escolha]

    # 5. Validação específica para divisão por zero
    if escolha == "4" and num2 == 0:
        while True:
            try:
                num2 = float(input("Divisão por zero não é permitida. Por favor, insira outro número: "))
                if num2 == 0:
                    print("Erro: Divisão por zero. Tente novamente.")
            except ValueError:
                print("Valor inválido! Por favor, digite apenas números.")

    # 6. Exceção do cálculo e exibição do resultado
    try:
        resultado = funcao_operacao(num1, num2)
        print(f"\nO resultado da {nome_operacao} é: {resultado}")
    except Exception as e:
        print(f"Erro ao realizar a operação: {e}")
    
    # 7. Condição de parada do loop principal
    continuar = input("\nDeseja realizar outra operação? (s/n): ").strip().upper()
    if continuar != 'S':
        print("Encerrando a calculadora. Até logo!")
        break
