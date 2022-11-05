class Persona2:
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.apellidos=input("Ingrese sus apellidos: ")
        
    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Apellidos", self.apellidos)
        
class Alumnos(Persona2):
    def __init__(self):
        super().__init__()
        self.matricula=input("Ingrese la matricula: ")
        
    def mostrarAlumno(self):
        super().mostrar()
        print("Matricula: ", self.matricula)
        
#Alumnos=Persona2()
#Alumnos.mostrar()
Alumno1=Alumnos()
Alumnos.mostrarAlumno()
