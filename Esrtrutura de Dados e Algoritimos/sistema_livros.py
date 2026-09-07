def obter_dados_livro(titulo, autor, quantidade):
    return f"{titulo} {autor} {quantidade}"

def obter_quantidade_livro(valor):
    try:
        qtd = int(valor)
        if qtd < 0:
            return "Por favor, insira um número válido para a quantidade."
        return qtd
    except ValueError:
        return "Por favor, insira um número válido para a quantidade."

def validar_livro_existe(biblioteca, titulo):
    if titulo in biblioteca:
        return True
    return f"Erro: O livro '{titulo}' não foi encontrado."

def adicionar_livro(biblioteca, titulo, autor, quantidade):
    if validar_livro_existe(biblioteca, titulo) == True:
        return f"Erro: O livro '{titulo}' já está cadastrado na biblioteca."
    biblioteca[titulo] = {"autor": autor, "quantidade": quantidade}
    return f"Livro '{titulo}' adicionado com sucesso"

def listar_livros(biblioteca):
    if not biblioteca:
        return "Não há livros cadastrados."
    livros_formatados = []
    for titulo, dados in sorted(biblioteca.items()):
        livros_formatados.append(f"{titulo} - {dados['autor']} - {dados['quantidade']}")
    return "\n".join(livros_formatados)

def remover_livro(biblioteca, titulo):
    validacao = validar_livro_existe(biblioteca, titulo)
    if validacao == True:
        del biblioteca[titulo]
        return f"Livro '{titulo}' removido com sucesso!"
    else:
        return validacao

def atualizar_quantidade(biblioteca, titulo, nova_quantidade):
    validacao = validar_livro_existe(biblioteca, titulo)
    if validacao == True:
        biblioteca[titulo] = biblioteca.get(titulo, {})
        biblioteca[titulo]["quantidade"] = nova_quantidade
        return f"Quantidade de exemplares do livro '{titulo}' atualizada para {nova_quantidade}"
    else:
        return validacao

def registrar_emprestimo(biblioteca, historico, titulo, quantidade):
    validacao = validar_livro_existe(biblioteca, titulo)
    if validacao == True:
        if biblioteca[titulo].get("quantidade", 0) >= quantidade:
            biblioteca[titulo]["quantidade"] -= quantidade
            historico.append((titulo, quantidade))
            return f"{quantidade} exemplares de '{titulo}' emprestados com sucesso!"
        else:
            return f"Erro: Estoque insuficiente para o livro '{titulo}'."
    else:
        return validacao

def obter_quantidade_livro_para_emprestimo(biblioteca, titulo, valor):
    try:
        qtd = int(valor)
        if qtd <= 0:
            return "Por favor, insira um número válido para a quantidade."
        elif qtd > biblioteca.get(titulo, {}).get("quantidade", 0):
            return f"Erro: Quantidade solicitada ({qtd}) é maior do que a disponível em estoque."
        else:
            return qtd
    except ValueError:
        return "Por favor, insira um número válido para a quantidade."

def exibir_historico_emprestimos(historico):
    if not historico:
        return "Não há histórico de empréstimos."
    return "\n".join([f"Livro: {item[0]} | Quantidade: {item[1]}" for item in historico])

def exibir_menu():
    return (
        "\n--- SISTEMA DE GERENCIAMENTO DE BIBLIOTECA ---\n"
        "1. Adicionar livro\n"
        "2. Listar livros\n"
        "3. Remover livro\n"
        "4. Atualizar quantidade de livros\n"
        "5. Registrar empréstimo\n"
        "6. Exibir histórico de empréstimos\n"
        "7. Sair"
    )

def menu():
    biblioteca = {}
    historico = []

    while True:
        print(exibir_menu())
        opcao = input("Digite a opção desejada (1-7): ").strip()

        if opcao == "1":
            titulo = input("Digite o título do livro: ").strip()
            autor = input("Digite o nome do autor: ").strip()

            quantidade = obter_quantidade_livro(input("Digite a quantidade de exemplares: "))
            if isinstance(quantidade, int):
                print(adicionar_livro(biblioteca, titulo, autor, quantidade))
            else:
                print(quantidade)

        elif opcao == "2":
            print("\n--- LIVROS CADASTRADOS ---")
            print(listar_livros(biblioteca))

        elif opcao == "3":
            titulo = input("Digite o título do livro a remover: ").strip()
            print(remover_livro(biblioteca, titulo))

        elif opcao == "4":
            titulo = input("Digite o título do livro: ").strip()
            quantidade = obter_quantidade_livro(input("Digite a nova quantidade total de exemplares: "))
            if isinstance(quantidade, int):
                print(atualizar_quantidade(biblioteca, titulo, quantidade))
            else:
                print(quantidade)

        elif opcao == "5":
            titulo = input("Digite o título do livro para empréstimo: ").strip()
            quantidade_emprestada = input("Digite a quantidade a ser emprestada: ")
            
            quantidade_valida = obter_quantidade_livro_para_emprestimo(biblioteca, titulo, quantidade_emprestada)
            if isinstance(quantidade_valida, int):
                print(registrar_emprestimo(biblioteca, historico, titulo, quantidade_valida))
            else:
                print(quantidade_valida)

        elif opcao == "6":
            print("\n--- HISTÓRICO DE EMPRÉSTIMOS ---")
            print(exibir_historico_emprestimos(historico))

        elif opcao == "7":
            print("Encerrando o sistema de biblioteca... Até logo!")
            break

        else:
            print("Opção inválida! Escolha um número entre 1 e 7.")

if __name__ == "__main__":
    menu()