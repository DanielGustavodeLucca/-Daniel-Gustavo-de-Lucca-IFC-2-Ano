class Cliente2():
     def __init__(self, pessoa, email):
        self.pessoa = pessoa
        self.email = email
     def __str__(self):
        return f"Pessoa: {self.pessoa}, Email: {self.email}"