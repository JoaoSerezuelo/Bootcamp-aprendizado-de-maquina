from functools import reduce

  
def mais_um_meio(nota):
    return nota+1.5

notas=[6.4, 7.2, 5.8, 8.6]
notas_finais=map(mais_um_meio, notas)

def somar(a,b):
    return a+b

'''
reduce recebe uma função e uma sequência e aplica a função acumulativamente
'''
total=reduce(somar, notas, 0)
print(total)

# print(notas_finais)
# print(list(notas_finais))#map retorna um iterador, por isso é necessário converter para lista


# for i, nota in enumerate(notas):
#     notas[i]=nota+1.5

# for i in range(len(notas)):
#     notas[i]=notas[i]+1.5