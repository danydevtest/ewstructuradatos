class Alumnos:
    def __init__(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota
        
    def imprimir(self):
        print("El nombre es: ",self.nombre)
        print("La nota es: ",self.nota)
        if(self.nota<7):
            print("No aprobado: ",self.nota)
        else:
            print("Aprobado: ",self.nota)
        
Alumno1=Alumnos("Dany",7)
Alumno1.imprimir()