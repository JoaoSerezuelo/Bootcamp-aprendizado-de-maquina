a='valor'
a = 0 # 0 é falso, qualquer outro valor é verdadeiro
a = '' # string vazia é falso, qualquer outra string é verdadeira
a=' '# string com espaço é verdadeira
a=[] # lista vazia é falso, qualquer outra lista é verdadeira
a={} # dicionário vazio é falso, qualquer outro dicionário é verdadeiro
 
 
if a:
    print("existe")
else:
    print("não existe")