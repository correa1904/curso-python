# def soma(a: int | None = 0, b: int | None = 0) -> int:
#     """
#         Essa função serve para somar 2 argumentos
#     :param a: número real inteiro.
#     :param b: número real inteiro.
#     :param c:
#     :param d:
#     :param e:
#     :return: a soma de a e b
#     """
#
#     return a + b

def soma(*args: int | None) -> int:
    """

    :param args: números inteiros que formarão um tupla
    :return: a soma de todos os números dessa tupla.
    """
    return sum(args)

res = soma(*args: 1, 2, 3, 4, 5, 6, 7, 8)
print(res)
