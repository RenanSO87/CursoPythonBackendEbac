class MoldePokemon:
    # Construtor da classe == > método especial que é chamado quando um objeto é criado a partir da classe
    # Ele é usado para inicializar os atributos do objeto
    # Self é uma referência ao próprio objeto que está sendo criado, permitindo acessar e modificar seus atributos e métodos
    def __init__(self, nome, altura, peso, hp, ataque, tipo,):
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.hp = hp
        self.ataque = ataque
        self.tipo = tipo

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Altura: {self.altura} m")
        print(f"Peso: {self.peso} kg")
        print(f"HP: {self.hp}")
        print(f"Ataque: {self.ataque}")
        print(f"Tipo: {self.tipo}")
    
    def mostrar_nome(self):
        print(f"O nome do Pokémon é {self.nome}.")

    def mostrar_tipo(self):
        print(f"{self.nome} é do tipo {self.tipo}.")
    
    def mostrar_ataque(self):
        print(f"{self.nome} tem um ataque de {self.ataque} pontos.")

    def mostrar_hp(self):
        print(f"{self.nome} tem {self.hp} pontos de HP.")

# Criando um objeto da classe MoldePokemon
pikachu = MoldePokemon("Pikachu", 0.4, 6.0, 35, 55, "Elétrico")
charizard = MoldePokemon("Charizard", 1.7, 90.5, 78, 84, "Fogo/Voador")
squirtle = MoldePokemon("Squirtle", 0.5, 9.0, 44, 48, "Água")
bulbasaur = MoldePokemon("Bulbasaur", 0.7, 6.9, 45, 49, "Grama/Veneno")

# Acessando os atributos do objeto
bulbasaur.mostrar_nome()
bulbasaur.mostrar_tipo()

pikachu.mostrar_nome()
pikachu.mostrar_tipo()

