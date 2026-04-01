class Triangulo:
    def __init__(self, b, a):

        self.base = b
        self.altura = a

    def area(self):
        return(self.base*self.altura)/2
    
print("===================================================")
t1 = Triangulo(10,5)
print(t1.base, t1.altura)
print((t1.base * t1.altura)/2)
print(t1.area())
print("===================================================")
t2 = Triangulo(20,10)
print(t2.base, t2.altura)
print((t2.base * t2.altura)/2)
print(t2.area())
print("===================================================")
listaTriangulos = [t1,t2]

for i in listaTriangulos:
    print(i.area())
print("===================================================")

for i in range (len(listaTriangulos)):
    print(listaTriangulos[i].area())
print("===================================================")
num = [10,20,30]

for i in range(len(num)):
    print(num[i], " = ", i)

print("===================================================")

for x in num:
    print(x)