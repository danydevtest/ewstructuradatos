class Persona:
    def inicializar(self,nombre,apellidos):
        self.nombre=nombre
        self.apellidos=apellidos
        
    def mostrarDatos(self):
        print("Nombre: ", self.nombre)
        print("Apellidos: ", self.apellidos)
        
#crear objetos
Alumnos=Persona()
Alumnos.inicializar("Dany","Cambrano")
Alumnos.mostrarDatos()

Alumnos=Persona()
Alumnos.inicializar("Pedro","Páramo")
Alumnos.mostrarDatos()
        