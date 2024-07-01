senha = input('Cadastre uma senha de 6 digitos: \n')

while len(senha) != 6:
    senha = input('Quantidade de char inválida \n'
                    'Cadastre uma senha de 6 digitos: \n')

print('Cadastro realizado com sucesso')
    