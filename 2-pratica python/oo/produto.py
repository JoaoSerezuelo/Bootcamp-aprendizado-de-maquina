class  Produto:
    def __init__(self, nome, preco=1.99, desconto=0):
        self.__nome=nome#__ "deixa privado"
        self.preco=preco
        self.desconto=desconto
    
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome=novo_nome
    
    @property #decorator pra transformar o metodo em propriedade
    def preco_final(self):
        return self.preco*(1-self.desconto)
    
    

p1=Produto('caneta', 6.5, 0.15) 
p2=Produto('caderno', 10, 0.2)


# print(p1._Produto__nome, p1.preco, p1.desconto, p1.preco_final)
# #acerssa o nome que tava privado
print(p2.nome, p2.preco, p2.desconto)
p2.nome='lapiseira'
print(p2.nome, p2.preco, p2.desconto)

