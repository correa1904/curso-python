idade = int(input('Entre com sua idade:'))

if idade >= 18:
    print('Pode dirigir!')
else:
    print('não pode dirigir!')


user = 'default user '

if input('Entre com usuário: ') == 'admin':
    print('Bem-vibdo!')
else:
    print('Usuário não tem as credenciais necessárias')
