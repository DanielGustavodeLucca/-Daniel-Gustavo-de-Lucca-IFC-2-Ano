
class Receita:
    def __init__(self, nome, tempo_preparo, ingredientes, modo_preparo):
        self.nome = nome
        self.tempo_preparo = tempo_preparo
        self.ingredientes = ingredientes
        self.modo_preparo = modo_preparo
    def __str__(self):
        return f'''
        Receita: {self.nome}
        Tempo de preparo: {self.tempo_preparo} minutos
        Modo de preparo: {self.modo_preparo}
        Ingredientes: {', '.join(self.ingredientes)}
        '''
class Ingrediente:
    def __init__(self, nome, quantidade, unidade):
        self.nome = nome
        self.quantidade = quantidade
        self.unidade = unidade
    def __str__(self):        
        return f"{self.quantidade} {self.unidade} de {self.nome}"
    


i1 = Ingrediente("farinha", 200, "g")
i2 = Ingrediente("leite", 300, "ml")
i3 = Ingrediente("ovo", 2, "unidades")
r1 = Receita("Panqueca", 15, [str(i1), str(i2), str(i3)], "Misture os ingredientes e cozinhe em uma frigideira.")

print(r1)
print (i1, i2, i3)