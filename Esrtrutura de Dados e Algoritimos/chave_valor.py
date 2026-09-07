# Dado um array inteiro, retorne verdadeiro se algum valor aparecer pelo menos duas vezes no array. 
# E retorne falso se cada elemento for distinto.

lista = [1, 1, 1, 3, 3, 4, 4, 5, 5]

elemento = {}

for num in lista:
 if num not in elemento:
  elemento[num] = 1
 else:
  elemento[num] += 1

for chave, valor in elemento.items():
 if valor >= 2:
  print("O elemento", chave, "aparece", valor, "vezes no array.")
  print("Retornando Verdadeiro")
 else:
  print("O elemento", chave, "aparece apenas uma vez no array.")
  print("Retornando Falso")
