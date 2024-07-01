nome = input('Entre com seu nome: ').title()
# TODO: Receber as notas

n1 = int(input("Entre com a nota da p1: "))
n2 = int(input("Entre com a nota da p2: "))

# TODO: calcular a média

media = (n1 + n2) / 2
print(f'sua média final é {media}.')

#  TODO: Dar o status a partir da media

if media == 10:
    print(f'{nome} foi aprovado com distinção!')
elif media >= 7:
    print(f'{nome} foi aprovado!')
else:
    print("Foi reprovado")


