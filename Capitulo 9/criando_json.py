import json

produtos = {
    'PS5': {
        'Id': 2022,
        'valor': 5000,
        'Quantidade': 100,
    },
    'God of war Ragnarock': {
        'ID': 2023,
        'Valor': 250,
        'Quantidade': 50
    }

}

with open('produtos.json', 'w') as meu_arquivo:
    json.dump(produtos, meu_arquivo)
    
with open('produtos.json', 'r') as arquivo:
    print(json.load(arquivo))