class Triangulo:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def retangulo(self):
        if (self.a^2 == self.b^2 + self.c^2) or (self.c^2 == self.b^2 + self.a^2) or (self.b^2 == self.a^2 + self.c^2):
            self.x = True
        else:
            self.x = False 
        return self.x
         
    def semelhantes(self,triangulo):
        a=[self.a,self.b,self.c]
        b=[triangulo.a,triangulo.b,triangulo.c]
        a.sort()
        b.sort()
        if a==b:
            x = True
        else:
            x = False
        return x