class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        return "O animal emirtiu um som genérico."
    
class Cachorro(Animal):
    def emitir_som(self):
        return " O cachorro latiu!"

class Gato(Animal):
    def emitir_som(self):
        return " O gato miou!"     