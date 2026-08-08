# Dicionário global que armazenará o estoque
estoque = {}

def adicionar_produto():
    print("\n--- Adicionar Produto ---")
    nome = input("Digite o nome do produto: ").strip()
    
    if nome in estoque:
        print(f"O produto '{nome}' já existe! Use a opção de atualizar quantidade.")
        return
    
    try:
        quantidade = int(input(f"Digite a quantidade de '{nome}': "))
        preco = float(input(f"Digite o preço de '{nome}': R$ "))
        
        # Armazenando o dicionário interno como valor da chave (nome do produto)
        estoque[nome] = {
            "quantidade": quantidade,
            "preço": preco
        }
        print(f"Produto '{nome}' adicionado com sucesso!")
    except ValueError:
        print("Erro: Quantidade deve ser um número inteiro e Preço deve ser um número decimal.")

def listar_produtos():
    print("\n--- Lista de Produtos ---")
    if not estoque:
        print("O estoque está vazio.")
        return
    
    # Ordenando o dicionário pelas chaves (nomes dos produtos) usando lambda
    # estoque.items() retorna tuplas (nome, dados). O lambda x: x[0] ordena pelo nome.
    produtos_ordenados = sorted(estoque.items(), key=lambda x: x[0].lower())
    
    for nome, dados in produtos_ordenados:
        print(f"{nome}: {dados['quantidade']} disponível(is) - R$ {dados['preço']:.2f}")

def remover_produto():
    print("\n--- Remover Produto ---")
    nome = input("Digite o nome do produto que deseja remover: ").strip()
    
    if nome in estoque:
        del estoque[nome]
        print(f"Produto '{nome}' removido com sucesso!")
    else:
        print(f"Erro: O produto '{nome}' no foi encontrado no estoque.")

def atualizar_quantidade():
    print("\n--- Atualizar Quantidade ---")
    nome = input("Digite o nome do produto: ").strip()
    
    if nome in estoque:
        try:
            nova_qtd = int(input(f"Digite a nova quantidade para '{nome}': "))
            estoque[nome]["quantidade"] = nova_qtd
            print(f"Quantidade do produto '{nome}' atualizada com sucesso!")
        except ValueError:
            print("Erro: A quantidade deve ser um número inteiro.")
    else:
        print(f"Erro: O produto '{nome}' não foi encontrado no estoque.")

def exibir_menu():
    print("\n========= MENU DE ESTOQUE =========")
    print("1. Adicionar produto")
    print("2. Listar produtos")
    print("3. Remover produto")
    print("4. Atualizar quantidade de produto")
    print("5. Sair")
    print("====================================")

# Função principal que controla o loop do programa
def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ").strip()
        
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            remover_produto()
        elif opcao == "4":
            atualizar_quantidade()
        elif opcao == "5":
            print("Saindo do programa... Até logo!")
            break
        else:
            print("Opção inválida! Por favor, escolha um número de 1 a 5.")

# Executa o programa
if __name__ == "__main__":
    main()