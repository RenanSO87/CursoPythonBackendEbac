def num_sorteado():
    from random import randint
    return randint(1, 100)

def palavra_sorteada():
    palavras = ['python', 'programação', 'sorteio', 'aleatório', 'desafio']
    for i in palavras:
        print(f'Palavra sorteada: {palavras}')


num = num_sorteado()
print(f'Número sorteado: {num}')
