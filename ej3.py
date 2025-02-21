class persona:
    def _init_(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.profesion}.")

p = persona("Ismael", 18 , "estudiante")
p.presentarse()

class estudiante(persona):
    def _init_(self, nombre, edad, profesion, grado):
        super()._init_(nombre, edad, profesion)
        self.grado = grado

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años, soy {self.profesion} y actualmente estudio en un grado de {self.grado}.")

e = estudiante("Manuel", 22, "jardinero", "jardinería")
e.presentarse()

class trabajador(persona):
    def _init_(self, nombre, edad, profesion, empresa):
        super()._init_(nombre, edad, profesion)
        self.empresa = empresa

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años, soy {self.profesion} y trabajo en {self.empresa}.")

t = trabajador("Antonio", 40, "jardinero", "Jardines Machado")
t.presentarse()