# Decorartor é uma função que recebe outra função como parâmetro e retorna uma nova função com funcionalidades adicionais.
# exemplo de um decorator simples que adiciona comportamento antes e depois da execução de uma função original.

def meu_decorator(funcao):
    def nova_funcao(*args, **kwargs):
        print("Antes de chamar a função original.")
        resultado = funcao(*args, **kwargs)
        print("Depois de chamar a função original.")
        return resultado
    return nova_funcao

@meu_decorator
def minha_funcao():
    print("Esta é a função original.") 

minha_funcao()

# Exemplo de um decorator que mede o tempo de execução de uma função.
import time

def medir_tempo(funcao):
    def nova_funcao(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução: {fim - inicio:.4f} segundos.")
        return resultado
    return nova_funcao

@medir_tempo
def funcao_lenta():
    time.sleep(2)  # Simula uma função que leva tempo para executar
    print("Função lenta executada.")

funcao_lenta()

# Decorators são úteis para adicionar funcionalidades a funções existentes sem modificar seu código original. 
# Eles são amplamente utilizados em frameworks e bibliotecas Python para implementar recursos como autenticação, logging, caching, entre outros.