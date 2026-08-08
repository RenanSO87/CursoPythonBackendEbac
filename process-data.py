def processar_dados(dados):
  processados = []
  for dado in dados:
    if isinstance(dado, int):
      processados.append(dado * 2)
    elif isinstance(dado, str):
      processados.append(dado.upper())
 
  return processados


dados = [1, 'hello', 2, 'world']
resultado = processar_dados(dados)
print(resultado)