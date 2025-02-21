class CuentaBancaria:
    def _init_(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def ver_saldo(self):
        return self.saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Has depositado {monto}. Nuevo saldo: {self.saldo}")
        else:
            print("El monto a depositar debe ser positivo.")

    def retirar(self, monto):
        if monto > 0:
            if monto <= self.saldo:
                self.saldo -= monto
                print(f"Has retirado {monto}. Nuevo saldo: {self.saldo}")
            else:
                print("Fondos insuficientes.")
        else:
            print("El monto a retirar debe ser positivo.")

cuenta = CuentaBancaria(10000)
print(f"Saldo inicial: {cuenta.ver_saldo()}")
cuenta.depositar(678)
cuenta.retirar(216)