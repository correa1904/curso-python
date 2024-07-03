
def bissexto(ano):
    if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

ano = 2024

if bissexto(ano):

    print(f"{ano} É um ano bissexto!")
else:
    print(f"{ano} Não é um ano bissexto!")