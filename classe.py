# Definindo a classe mãe (Superclasse)

class Animal:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print("O animal emite um som genérico.")

# Definindo a classe Cachorro que herda de Animal (Subclasse)

class Cachorro(Animal):
    def emitir_som(self):
        print("O cachorro latiu!")

# Definindo a classe Gato que herda de Animal (Subclasse)

class Gato(Animal):
    def emitir_som(self):
        print("O gato miou!")

# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    # Criando um objeto da classe Cachorro
    dog = Cachorro(nome="Thor", idade=3)
    
    # Criando um objeto da classe Gato
    cat = Gato(nome="Mingau", idade=2)

    # Exibindo os dados e chamando o método emitir_som para o cachorro
    print(f"Cachorro -> Nome: {dog.nome}, Idade: {dog.idade} anos")
    dog.emitir_som()

    print("-" * 30)

    # Exibindo os dados e chamando o método emitir_som para o gato
    print(f"Gato -> Nome: {cat.nome}, Idade: {cat.idade} anos")
    cat.miar = cat.emitir_som()  # O método já faz o print internamente, então não é necessário atribuir a uma variável