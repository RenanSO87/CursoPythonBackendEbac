# Definimos o uso de letras maiúsculas e minúsculas em uma palavra como correto quando o seguinte caso é válido:
# Todas as letras são maiúsculas, como "EUA".
# Dada uma palavra de string, retorne true se a capitalização da palavra for correta.

palavra = "GATi"

contador = 0

for letra in palavra:
 if letra.isupper():
  contador += 1

print("A palavra é:", palavra)
print(contador)
print(len(palavra))

if contador == len(palavra) or contador == 0 or (contador == 1 and palavra[0].isupper()):
 print("Palavra com capitalização correta")

else:
 print("Palavra com capitalização incorreta")
