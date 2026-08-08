class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f"{self.nome} está comendo!")
    
    
class Cachorro(Animal):

    def latir(self):
        print(f"{self.nome} está latindo!")

meu_cachorro = Cachorro("Rex")

meu_cachorro.comer()  # Método herdado da classe Animal
meu_cachorro.latir()  # Método específico da classe Cachorro

