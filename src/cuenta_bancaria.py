class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, saldo):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.tipo_interes = 1.5

    def get_titular(self):
        return self.titular

    def set_titular(self, titular):
        self.titular = titular

    def get_numero_cuenta(self):
        return self.numero_cuenta

    def get_saldo(self):
        return self.saldo

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
        else:
            print("La cantidad a ingresar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
            else:
                print("No hay suficiente saldo en la cuenta.")
        else:
            print("La cantidad a retirar debe ser positiva.")

    def calcular_interes(self):
        return self.saldo + (self.saldo * self.tipo_interes / 100)

    def set_tipo_interes(self, tipo_interes):
        if 0 <= tipo_interes <= 10:
            self.tipo_interes = tipo_interes
        else:
            print("El tipo de interés debe estar entre 0% y 10%.")