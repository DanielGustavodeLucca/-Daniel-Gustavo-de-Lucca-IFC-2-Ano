class Receita:
    
    def __init__(self, nome, tempo_preparo, modo_preparo):
        self.nome = nome
        self.tempo_preparo = tempo_preparo
        self.modo_preparo = modo_preparo
    # como expressar uma receita em formato textual        
    def __str__(self):
        return f'''
        Receita: {self.nome}
        Tempo de preparo: {self.tempo_preparo} minutos
        Como preparar: {self.modo_preparo}
        '''

class Ingrediente:
    def __init__(self,nome):
        self.nome=nome

class IngredienteDaReceita:
    def __init__(self, receita, ingrediente, quantidade, unidade):
        self.receita = receita
        self.ingrediente = ingrediente
        self.quantidade = quantidade
        self.unidade = unidade

# teste da classe

r1 = Receita("Bolo de Milho", 50,
              "Bater tudo no liquidificador e colocar no forno")    

r2 = Receita("Massa de pizza", 15,
              "LOREM IPSUM ETC...")    

i1= Ingrediente("Milho")
i2= Ingrediente("Leite")
i3= Ingrediente("Açúcar")
i4= Ingrediente("Ovos")
i5= Ingrediente("Óleo")
i6= Ingrediente("Fermento")

i7= Ingrediente("Farinha de Trigo")
i8= Ingrediente("Fermento Biológico")
i9= Ingrediente("Sal")
i10= Ingrediente("Água Morna")
i11= Ingrediente("Pinga")

# registrar que na receita 1 vai ter uma lata de milho
ir1 = IngredienteDaReceita(r1, i1, 1, "lata")
ir2 = IngredienteDaReceita(r1, i2, 1, "lata")
ir3 = IngredienteDaReceita(r1, i3, 1, "lata")
ir4 = IngredienteDaReceita(r1, i4, 3, "unidade")
ir5 = IngredienteDaReceita(r1, i5, 0.5, "lata")
ir6 = IngredienteDaReceita(r1, i6, 1, "colher de chá")

ir7 = IngredienteDaReceita(r2, i7, 1, "kg")
ir8 = IngredienteDaReceita(r2, i8, 30, "g")
ir9 = IngredienteDaReceita(r2, i5, 3, "xicaras")
ir10 = IngredienteDaReceita(r2, i10, 3, "xicaras")
ir11 = IngredienteDaReceita(r2, i9, 1, "colher de chá")
ir12 = IngredienteDaReceita(r2, i3, 1, "colher de chá")
ir13 = IngredienteDaReceita(r2, i11, 1, "colher de sopa")

irs = [ir1, ir2, ir3, ir4, ir5, ir6]
print(r1) # .nome, r1.tempo_preparo, r1.modo_preparo)
#print(ir1, ir2, ir3, ir4, ir5, ir6)

for ir in irs:
    print(ir.ingrediente.nome, ir.quantidade, ir.unidade)

irs2 = [ir7, ir8, ir9, ir10, ir11, ir12, ir13]
print(r2) # .nome, r1.tempo_preparo, r1.modo_preparo)
#print(ir1, ir2, ir3, ir4, ir5, ir6)

for ir in irs2:
    print(ir.ingrediente.nome, ir.quantidade, ir.unidade)