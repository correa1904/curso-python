alunos_notas = {'Joao': [7, 4, 5], 'Maria': [5, 8, 9],
                'Leo': [6, 7, 7], 'Pedro': [7, 4, 10]}

alunos_aprovados = dict(filter(lambda alunos: [alunos[0] for alunos in alunos_notas.items()
                    if round(sum(alunos[1])/len(alunos[1]), 2) >= 7]

print(alunos_aprovados)