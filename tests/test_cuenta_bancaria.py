import unittest
from cuenta_bancaria import CuentaBancaria

class TestCuentaBancaria(unittest.TestCase):
    
    def setUp(self):
        # Inicializa una cuenta bancaria antes de cada prueba
        self.cuenta = CuentaBancaria("Juan Pérez", "12345678", 1000.0)

    def test_get_titular(self):
        # Prueba si el método get_titular() devuelve el titular correcto
        self.assertEqual(self.cuenta.get_titular(), "Juan Pérez")

    def test_set_titular(self):
        # Prueba si el método set_titular() actualiza correctamente el titular
        self.cuenta.set_titular("Ana Gómez")
        self.assertEqual(self.cuenta.get_titular(), "Ana Gómez")

    def test_get_numero_cuenta(self):
        # Prueba si el método get_numero_cuenta() devuelve el número de cuenta correcto
        self.assertEqual(self.cuenta.get_numero_cuenta(), "12345678")

    def test_get_saldo(self):
        # Prueba si el saldo inicial es correcto
        self.assertEqual(self.cuenta.get_saldo(), 1000.0)

    def test_ingresar(self):
        # Prueba si el método ingresar() actualiza correctamente el saldo
        self.cuenta.ingresar(500.0)
        self.assertEqual(self.cuenta.get_saldo(), 1500.0)

    def test_ingresar_cantidad_negativa(self):
        # Prueba si no se permite ingresar una cantidad negativa
        self.cuenta.ingresar(-200.0)
        self.assertEqual(self.cuenta.get_saldo(), 1000.0)  # El saldo no debe cambiar

    def test_retirar(self):
        # Prueba si el método retirar() actualiza correctamente el saldo
        self.cuenta.retirar(300.0)
        self.assertEqual(self.cuenta.get_saldo(), 700.0)

    def test_retirar_cantidad_insuficiente(self):
        # Prueba si no se permite retirar una cantidad mayor al saldo disponible
        self.cuenta.retirar(1200.0)
        self.assertEqual(self.cuenta.get_saldo(), 1000.0)  # El saldo no debe cambiar

    def test_calcular_interes(self):
        # Prueba si el método calcular_interes() funciona correctamente
        self.assertEqual(self.cuenta.calcular_interes(), 1015.0)  # Asume un interés del 1.5%

    def test_set_tipo_interes(self):
        # Prueba si el método set_tipo_interes() establece correctamente el nuevo tipo de interés
        self.cuenta.set_tipo_interes(5.0)
        interes_esperado = self.cuenta.get_saldo() * 5.0 / 100
        self.assertEqual(self.cuenta.calcular_interes(), interes_esperado + self.cuenta.get_saldo())

    def test_set_tipo_interes_invalido(self):
        # Prueba si no se permite establecer un tipo de interés fuera del rango permitido
        self.cuenta.set_tipo_interes(15.0)  # valor fuera de rango
        self.assertEqual(self.cuenta.calcular_interes(), 1015.0)  # El tipo de interés no debería cambiar

if __name__ == "__main__":
    unittest.main()
