class Calculadora:
     def __init__(self ):
         self.valor1=int(input("Ingresa el valor 1: "))
         self.valor2=int(input("Ingresa el valor 2: "))
     def Suma(self):
         return (self.valor1+self.valor2)
     def Resta(self):
         return (self.valor1-self.valor2)
     
     def imprimir(self):
         print("La suma es: ",self.Suma())
         print("La resta es: ",self.Resta())
        
operaciones=Calculadora()
operaciones.Suma()
operaciones.Resta()
operaciones.imprimir()