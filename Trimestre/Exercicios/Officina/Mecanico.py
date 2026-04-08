from Pessoa import *

class Mecanico:
    def __init__(self, pessoa: Pessoa):
        self.pessoa = pessoa
    def __str__(self):
        return f'''
        Mecanico: {self.pessoa}
        '''