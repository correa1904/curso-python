# Função para determinar o tipo de triangulo
# TODO: Receber 3 lados do triangulo

a = int(input('mostre o valor a:'))
b = int(input('mostre o valor b:'))
c = int(input('mostre o valor c:'))

# TODO: Verificar se é um triangulo

if (a + b + c) or (b + c > a) or (c + a > b):
    print('É um triangulo.')

# TODO: Verificar o tipo

if a == b == c:
    print('Equilátero.')
elif a == b or a == c or b == c:
    print('Isóceles.')
elif a != b or b != c or c != a:
    print('Escaleno.')