
a = 3
b = 4


def soma():
    a = int(input('Entre com a: '))
    b = int(input('Entre com b: '))
    return a + b

def area_circunferencia():

    raio = float(input('Entre com o raio da circunferencia:'))
    pi = 3.14

    return pi*raio**2

resultado = area_circunferencia()

print(resultado)
