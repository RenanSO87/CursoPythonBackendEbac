# Retorne a média de todos os salários, com exceção do salário mínimo e máximo.

salarios = [9000, 13000, 15000, 2000, 5399.89,53000]

salario_atual = sorted(salarios)

print("Salários ordenados:", salario_atual)

salario_atual.remove(max(salario_atual))
salario_atual.remove(min(salario_atual))

media = sum(salario_atual) // len(salario_atual)

print("A quantidade de valores para a média salarial são", len(salario_atual))
print("A média dos salários, excluindo o mínimo e o máximo, é:", media)
