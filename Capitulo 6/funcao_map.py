# def dobro(num):
#     return num * 2


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i, numero in enumerate(lista):
#     lista[i] = dobro(numero)
#
# print(lista)

lista_dobro = list(map(lambda x: x * 2, lista))

print(lista_dobro)