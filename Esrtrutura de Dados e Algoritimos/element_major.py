# Dado um array de elementos n, retorne o elemento majoritário
# Ou seja, o elemento que aparece mais da metade das vezes no array.
# Elemento majoritário é o elemento que aparece mais de n/2 vezes no array.
# O elemento majoritário sempre existe no array.

elementos = [3, 2, 3]
num_elementos = len(elementos)
item_majoritario = num_elementos / 2

contador = {}

for item in elementos:
 if item not in contador:
  contador[item] = 1
 else:
  contador[item] += 1

print("Contagem de elementos:", contador)

for elemento, contagem in contador.items():
 if contagem >= item_majoritario:
  print("O elemento majoritário é:", elemento)
  