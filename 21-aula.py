# Yield
# O yield é uma palavra-chave em Python que é usada para criar geradores. Um gerador é uma função que pode ser pausada e retomada, permitindo que você produza uma sequência de valores ao longo do tempo, em vez de calcular todos os valores de uma vez e armazená-los na memória.
# 
# A principal vantagem dos geradores é que eles são mais eficientes em termos de memória, pois produzem um valor de cada vez, em vez de armazenar toda a sequência na memória. Isso é especialmente útil quando você está lidando com grandes conjuntos de dados ou sequências infinitas.

def contador(max):
    count = 0
    while count < max:
        yield count  # Pausa a função e retorna o valor atual de count
        count += 1

# Criando um gerador
meu_contador = contador(5)

# Iterando sobre o gerador
for numero in meu_contador:
    print(numero)
# Saída:
# 0
# 1
# 2
# 3
# 4

# O yield é uma maneira poderosa de criar iteradores personalizados e pode ser usado para simplificar o código que lida com sequências de dados. Ele é especialmente útil em situações onde você deseja gerar uma sequência de valores sob demanda, sem precisar armazenar toda a sequência na memória.
