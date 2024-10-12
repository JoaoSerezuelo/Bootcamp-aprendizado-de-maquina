class Carro:
    def __init__(self):
        self.__velocidade=0
    
    @property    
    def velocidade(self):
        return self.__velocidade
        
    def acelerrar(self):
        self.__velocidade+=5
        return self.__velocidade
    
    def frear(self):
        self.__velocidade-=5
        return self.__velocidade

class Uno(Carro):
    pass

class Ferrari(Carro):
    def acelerrar(self):
        super().acelerrar()
        return super().acelerrar()
    
    
  
# c1=Carro()
# print(c1.acelerrar())
# print(c1.acelerrar())
# print(c1.acelerrar())
# print(c1.frear())
# print(c1.frear())

c1=Uno()
print(c1.acelerrar())
print(c1.acelerrar())
print(c1.acelerrar())
print(c1.frear())
print(c1.frear())

