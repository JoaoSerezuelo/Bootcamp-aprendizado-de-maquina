def soma(*nums):
    total=0
    for n in nums:
        total+=n
    return total

def resultado_final(**kwargs):
    status='Aprovado' if kwargs['nota']>=6 else 'Reprovado'
    return f'aluno: {kwargs["nome"]} está {status} com nota {kwargs["nota"]}'
    