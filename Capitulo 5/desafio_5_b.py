s = set()

while True:

    item = input('Inorme o nome do item (ou enter para sair): ')
    if item:
        s.add(int(item))
        continue
    else:
        break
      
lista_final = list(sorted(s))

print(lista_final)