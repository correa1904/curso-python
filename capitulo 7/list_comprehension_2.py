
lista_pares = [n for n in range(0, 51) if n % 2 == 0]

print(lista_pares)

alunos_notas = {'Joao': [7, 4, 5], 'Maria': [5, 8, 9],
                'Leo': [6, 7, 7], 'Pedro': [7, 4, 10]}

aprovados = [aluno[0] for aluno in alunos_notas.items()
             if round(sum(aluno[1])/len(aluno[1]), 2) >= 7]

print(aprovados)

lista_dados = [n if n % 2 == 0 else 'impar' for n in range(1, 51)]

print(lista_dados)

staus_alunos = [aluno[0] if round(sum(aluno[1]), 2) >= 7
                else "Recuperação" for aluno in alunos_notas.items()]

print(staus_alunos)
