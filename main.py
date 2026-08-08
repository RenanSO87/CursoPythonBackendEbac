def calcular_area_retangulo(largura, altura):
    return largura * altura

def calcular_area_circulo(raio):
    import math
    return math.pi * raio ** 2

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

# Exemplo de uso

largura = 5
altura = 10
area_retangulo = calcular_area_retangulo(largura, altura)
print(f"A área do retângulo é: {area_retangulo}")
raio = 3
area_circulo = calcular_area_circulo(raio)
print(f"A área do círculo é: {area_circulo}")
base = 4
altura_triangulo = 6
area_triangulo = calcular_area_triangulo(base, altura_triangulo)
print(f"A área do triângulo é: {area_triangulo}")
