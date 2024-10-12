class Contador:
    contador=0 #atributo de classe
    
    @classmethod
    def inc(cls):
        cls.contador+=1
        return cls.contador
    
    @classmethod
    def dec(cls):
        cls.contador-=1
        return cls.contador
    
    def inst(self):
        return 'instancia'
    
    @staticmethod
    def mais_um(n):
        return n+1
    
print(Contador.inc())
print(Contador.inc())
print(Contador.dec())
print(Contador.dec())
# c1=Contador()
# print(c1.inst())
print(Contador.mais_um(5)) 