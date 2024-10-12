from functools import reduce

alunos = [
    {'nome': 'Pedro', 'nota': 9.8},
    {'nome': 'Maria', 'nota': 8.5},
    {'nome': 'João', 'nota': 7.2},
    {'nome': 'Ana', 'nota': 6.5},
    {'nome': 'José', 'nota': 5.0},
]


somar=lambda a,b: a+b

alunos_aprovados=[aluno['nota'] for aluno in alunos if aluno['nota']>=7]
notas_alunos_aprovados=[aluno['nota'] for aluno in alunos if aluno['nota']>=7]
total=reduce(somar, notas_alunos_aprovados, 0)

print(notas_alunos_aprovados)
print(total)