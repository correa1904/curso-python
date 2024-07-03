def atualiza_estoque(**kwargs):
    print('\n-------Vamos atualizar o estoque do sistema-------')
    estoque = {}
    for item, quantidade in kwargs.items():
        estoque[item] = quantidade
    print('\n-----Resumo do estoque-----\n')
    if len(estoque) > 0:
        for produto, quantidade in estoque.items():
            print(f'{produto}: {quantidade} unidades.')
        print(f'\nTemos um total de {sum(estoque.values())} produtos no estoque.')
    else:
        print('O estoque está vazio')

atualiza_estoque(banana=2, maca=3)