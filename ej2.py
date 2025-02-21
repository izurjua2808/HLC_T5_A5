class persona:
    def _init_(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.profesion}.")

p = persona("Ismael", 18 , "alumno")
p.presentarse()

class estudiante(persona):
    def _init_(self, nombre, edad, profesion, grado):
        super()._init_(nombre, edad, profesion)
        self.grado = grado

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años, soy {self.profesion} y estudio en el grado de {self.grado}.")

e = estudiante("Pablo", 40, "mecánico", "mecánica")
e.presentarse()