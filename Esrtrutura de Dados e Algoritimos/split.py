# Dado uma frase, que consite em palavras e espaços, retorne o comprimemto 
# da última palavra da string.

frase = "fly me to the moon"
ultima_palavra = frase.split()
print(ultima_palavra)

print(len(ultima_palavra[-1]))
print("O comprimento da última palavra é:", len(ultima_palavra[-1]))
