def Fahrenheit():

    c = int(input(f'Entre com a temperatura: \n'))
    f = (c * 1.8) + 32

    return f

resultado = Fahrenheit()

print(resultado)