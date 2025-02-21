class Figura:
    def calcular_area(self):
        pass

class Circulo(Figura):
    def _init_(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * (self.radio ** 2)

class Rectangulo(Figura):
    def _init_(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

circulo = Circulo(5)
print(f"Área del círculo: {circulo.calcular_area()}")

rectangulo = Rectangulo(4, 6)
print(f"Área del rectángulo: {rectangulo.calcular_area()}")