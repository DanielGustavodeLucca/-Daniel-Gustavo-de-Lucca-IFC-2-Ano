class Veiculo():
    def __init__(self, placa, cor, tanque: int, odometro: float, rendimento: float, desenho):
        self.placa = placa
        self.cor = cor
        self.tanque = tanque
        self.odometro = odometro
        self.rendimento = rendimento
        self.desenho = desenho

    def __str__(self):
        return f"Placa: {self.placa}, Cor: {self.cor}, Tanque: {self.tanque}, Odometro: {self.odometro}, rendimento: {self.rendimento}, desenho: {self.desenho}"
    
    def andar(self):
    #diminuir 1 do tanque
        self.tanque = self.tanque-1
    #acrescentar no odometro a kilometragem percorrida com 1 litro(rendimento)
        self.odometro = self.odometro+self.rendimento

class Pista:
    def __init__(self, extensao: int, veiculos):
        self.extensao = extensao
        self.veiculos = []
    
    def __str__(self):
        return f"Extensão: {self.extensao}, Veiculos: {self.veiculos}"

        