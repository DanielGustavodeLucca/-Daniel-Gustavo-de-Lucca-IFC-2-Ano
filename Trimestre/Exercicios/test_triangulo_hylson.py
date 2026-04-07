# importar a biblioteca de testes
import unittest
from triangulo import *
# a classe de teste deve herdar de unittest.TestCase
class TestTriangle(unittest.TestCase):

    def test_area(self):
        t1 = Triangulo(10,5)
        self.assertEqual(t1.area(),25)

    def test_valores(self):
        t1 = Triangulo(10,5)
        self.assertEqual(t1.base, 10)
        self.assertEqual(t1.altura, 15)
'''
    # nome do método de teste deve iniciar com 'test_'
    def test_soma(self):
        resultado = somar(2, 2)
        # aqui consiste no teste, comparando resultado esperado com o real
        self.assertEqual(resultado, 4) 
        # existem também:
        
        self.assertNotEqual(resultado, 5) # verifica se resultado é diferente de 5
        self.assertTrue(resultado == 4) # verifica se resultado é True
        self.assertFalse(resultado == 5) # verifica se resultado é False
        self.assertIsNone(resultado) # verifica se resultado é None
        

    def test_soma_negativa(self):
        resultado = somar(-1, -1)
        self.assertEqual(resultado, -2)

    def test_fatorial(self):
        resultado = fatorial(5)
        self.assertEqual(resultado, 120)

    def test_fatorial_zero(self):
        resultado = fatorial(0)
        self.assertEqual(resultado, 1)

    def test_fatorial_negativo(self):
        resultado = fatorial(-1)
        self.assertEqual(resultado, -1)
'''
if __name__ == '__main__':
    # executa os testes
    unittest.main()