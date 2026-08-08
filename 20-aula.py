# List Comprehension

# Gerar uma lista de números de 1 a 10
numeros = [x for x in range(1,11)]
print(numeros)

# Gerar uma lista de quadrados de números de 1 a 10
quadrados = [x**2 for x in range(1, 11)]
print(quadrados)

# Gerar uma lista de números pares de 1 a 20
pares = [x for x in range(1, 21) if x % 2 == 0]
print(pares)

# Gerar uma lista de palavras em uma frase
frase = "Python é uma linguagem de programação"
palavras = [palavra for palavra in frase.split()]
print(palavras)

# Gerar uma lista de letras em uma palavra
palavra = "Python"
letras = [letra for letra in palavra]
print(letras)
