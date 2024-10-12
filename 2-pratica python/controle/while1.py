# x=0

# while x!=-1:
#     x=float(input('Digite um numero (-1 pra sair): '))
    
# print('Fim do programa')

total=0
quantidade=0
nota=0

while nota!=-1:
    nota=float(input('Digite a nota do aluno (-1 pra sair): '))
    if nota!=-1:
        total+=nota
        quantidade+=1
        
print('Media: %.2f' % (total/quantidade))