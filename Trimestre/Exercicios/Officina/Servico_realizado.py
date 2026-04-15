class Servico_realizado():
    def __init__(self, servico, mecanico):
        self.servico = servico
        self.mecanico = mecanico

    def __str__(self):
            return f'''
Os dados do serviço realizado são ----------------> {self.servico}
{self.mecanico}

'''