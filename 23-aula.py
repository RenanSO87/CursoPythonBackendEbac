# Função Lambda
# Funções lambda são funções anônimas em Python, ou seja, funções que não possuem um nome definido. 
# Elas são úteis para criar funções simples e rápidas, geralmente usadas como argumentos para outras funções.
# A sintaxe básica de uma função lambda é a seguinte:
# lambda argumentos: expressão

# Exemplo de uma função lambda que soma dois números
soma = lambda x, y: x + y
print(soma(5, 3))  # Saída: 8

# Exemplo de uma função lambda que verifica se um número é par
eh_par = lambda x: x % 2 == 0
print(eh_par(4))  # Saída: True
print(eh_par(5))  # Saída: False

# Exemplo de uma função lambda que retorna o quadrado de um número
quadrado = lambda x: x ** 2
print(quadrado(6))  # Saída: 36

# Exemplo de uma função lambda com map, filter e reduce
from functools import reduce

# Usando map para aplicar uma função lambda a cada elemento de uma lista
numeros = [1, 2, 3, 4, 5]

# Usando map para aplicar uma função lambda a cada elemento de uma lista
quadrados = list(map(lambda x: x ** 2, numeros))
print(quadrados)  # Saída: [1, 4, 9, 16, 25]

# Usando filter para filtrar elementos de uma lista com base em uma condição
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Saída: [2, 4]

# Usando reduce para reduzir uma lista a um único valor
soma_total = reduce(lambda x, y: x + y, numeros)
print(soma_total)  # Saída: 15
