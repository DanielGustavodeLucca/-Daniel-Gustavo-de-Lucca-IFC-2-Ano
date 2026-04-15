from Pessoa import *
from Cliente import *
from Cliente2 import *
from Mecanico import *
from Servico import *
from Servico_realizado import *
from Ordem_Servico import *

class Veiculo():
    def __init__(self, placa, cor):
        self.placa = placa
        self.cor = cor

    def __str__(self):
        return f"Placa: {self.placa}, Cor: {self.cor}"
        
class Moto(Veiculo):
    def __init__(self, placa, cor):
        super().__init__(placa, cor)

    def __str__(self):
        return f"{super().__str__()}"

class VeiculoComPassageiro(Veiculo):
    def __init__(self, placa, cor, lugares):
        super().__init__(placa, cor)
        self.lugares = lugares

    def __str__(self):
        return f"{super().__str__()}, Lugares: {self.lugares}"
        
class Carro(VeiculoComPassageiro):
    def __init__(self, placa, cor, lugares, portas):
        super().__init__(placa, cor, lugares)
        self.portas = portas

    def __str__(self):
        return f"{super().__str__()}, Portas: {self.portas}"

class Onibus(VeiculoComPassageiro):
    def __init__(self, placa, cor, lugares):
        super().__init__(placa, cor, lugares)

    def __str__(self):
        return f"{super().__str__()}"




pess1 = Pessoa("João", "(47)123456", "28/01/2010")
pess2 = Pessoa("Mario", "(47)654321", "02/12/2009")
mec1 = Mecanico(pess2)
cli1 = Cliente(pess1, "joao.joao@gmail.com")
cli2 = Cliente2(pess1, "joao.joao@gmail.com")
car1 = Carro("ythh-4534634", "branco", 5, 4)
mot1 = Moto("gfhfg-2353456435474356", "preto")
ser1 = Servico("troca de pneu", 250)
ser2 = Servico("troca de óleo", 100)
ser3 = Servico("aibarg estourou", 3000)
ser4 = Servico("fundiu o motor", 6000)
ser5 = Servico("Perda de potência/Falhas", 100)
serre1 = Servico_realizado(ser1, mec1)
serre2 = Servico_realizado(ser2, mec1)
serre3 = Servico_realizado(ser3, mec1)
serre4 = Servico_realizado(ser4, mec1)
serre5 = Servico_realizado(ser5, mec1)

lstser = [serre1, serre2, serre3, serre4, serre5]
ord_ser = Ordem_servico("25/04/2026", car1, "26/04/2026", cli1, 20, lstser)

print(ord_ser)
print(mot1)
print(pess1)
print(mec1)
print("cliente que mais gastou: João")