with open('anna_julia.txt', 'r', encoding='utf-8') as file:
    conta_Anna = 0
    for linha in file.readlines():
        if 'Anna' in linha:
            conta_Anna += 1

print(conta_Anna)


