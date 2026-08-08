# calculadora.py

def executar_calculadora():
    while True:
        print("Calculadora Simples")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Escolha uma operação (1-5): ")

        if escolha == '5':
            print("Saindo da calculadora.")
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            resultado = num1 + num2
            print(f"Resultado: {resultado}")
        elif escolha == '2':
            resultado = num1 - num2
            print(f"Resultado: {resultado}")
        elif escolha == '3':
            resultado = num1 * num2
            print(f"Resultado: {resultado}")
        elif escolha == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado: {resultado}")
            else:
                print("Erro: Divisão por zero não é permitida.")
        else:
            print("Opção inválida. Por favor, escolha uma operação vál2ida.")