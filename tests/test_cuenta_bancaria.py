import unittest
from cuenta_bancaria import CuentaBancaria

class TestCuentaBancaria(unittest.TestCase):
    
    def setUp(self):
      
        self.cuenta = CuentaBancaria("Juan Pérez", "12345678", 1000.0)

    def test_get_titular(self):
      
        self.assertEqual(self.cuenta.get_titular(), "Juan Pérez")

    def test_set_titular(self):
        
        self.cuenta.set_titular("Ana Gómez")
        self.assertEqual(self.cuenta.get_titular(), "Ana Gómez")

    def test_get_numero_cuenta(self):
        
        self.assertEqual(self.cuenta.get_numero_cuenta(), "12345678")

    def test_get_saldo(self):
       
        self.assertEqual(self.cuenta.get_saldo(), 1000.0)

    def test_ingresar(self):
        
        self.cuenta.ingresar(500.0)
        self.assertEqual(self.cuenta.get_saldo(), 1500.0)

    def test_ingresar_cantidad_negativa(self):
      
        self.cuenta.ingresar(-200.0)
        self.assertEqual(self.cuenta.get_saldo(), 1000.0)  

    def test_retirar(self):
        
        self.cuenta.retirar(300.0)
        self.assertEqual(self.cuenta.get_saldo(), 700.0)

    def test_retirar_cantidad_insuficiente(self):
        
        self.cuenta.retirar(1200.0)
        self.assertEqual(self.cuenta.get_saldo(), 1000.0)  

    def test_calcular_interes(self):
       
        self.assertEqual(self.cuenta.calcular_interes(), 1015.0)  

    def test_set_tipo_interes(self):
        
        self.cuenta.set_tipo_interes(5.0)
        interes_esperado = self.cuenta.get_saldo() * 5.0 / 100
        self.assertEqual(self.cuenta.calcular_interes(), interes_esperado + self.cuenta.get_saldo())

    def test_set_tipo_interes_invalido(self):
       
        self.cuenta.set_tipo_interes(15.0)  
        self.assertEqual(self.cuenta.calcular_interes(), 1015.0) 

if __name__ == "__main__":
    unittest.main()
