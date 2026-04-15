class Ordem_servico():
    def __init__(self, data_entrada, veiculo, data_saida, cliente, desconto, servicos):
        self.data_entrada = data_entrada
        self.veiculo = veiculo
        self.data_saida = data_saida
        self.cliente = cliente
        self.desconto = desconto
        self.servicos = servicos
    
    def CalularTotal(self):
        total = 0
        for i in self.servicos:
            total = total + i.servico.valor
        total=total-self.desconto
        return total
    
    def printarServicos(self):
        a = ""
        for i in self.servicos:
            a = a + f"{i.servico.descricao};"
        return a

    def __str__(self):
        return f"Entrada: {self.data_entrada}, {self.veiculo}, Saida: {self.data_saida}, Cliente: {self.cliente.pessoa.nome}, Desconto: {self.desconto}, serviços realizados: {self.printarServicos()}, Total: {self.CalularTotal()}" 