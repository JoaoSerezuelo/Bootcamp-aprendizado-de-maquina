numero=3
numero2=4.4
print(numero+numero2)
texto='idade: '
idade=23
#print(texto+idade)#vai dar erro pq nao pode concatenar string com inteiro
print(texto+str(idade))#converte o inteiro para string
print(f'{texto}{idade}')#f-string
print(3*'oi')#vai repetir a string 3 vezes

PI=3.14 #não tem constante em python, mas por convenção usa-se letras maiusculas para variaveis que não devem ser alteradas
raio=float(input('Digite o raio do circulo: '))#função para receber um input do usuario, e o float converte o input para float
print(type(raio))# type mostra o tipo da variavel
#area=PI*raio*raio
area=PI*pow(raio,2)#função pow eleva o primeiro argumento ao segundo
print(f'A área do circulo é {area}')
