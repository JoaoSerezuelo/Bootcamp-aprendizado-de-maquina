from functools import reduce

alunos = [
    {'nome': 'Pedro', 'nota': 9.8},
    {'nome': 'Maria', 'nota': 8.5},
    {'nome': 'João', 'nota': 7.2},
    {'nome': 'Ana', 'nota': 6.5},
    {'nome': 'José', 'nota': 5.0},
]

aluno_aprovado=lambda aluno: aluno['nota']>=7
obter_nota=lambda aluno: aluno['nota']
somar=lambda a,b: a+b

alunos_aprovados=filter(aluno_aprovado, alunos)
notas_alunos_aprovados=map(obter_nota,alunos_aprovados)
total=reduce(somar, notas_alunos_aprovados, 0)

# print(list(alunos_aprovados))
# print(obter_nota(alunos[0]))
print(list(notas_alunos_aprovados))
print(total)

