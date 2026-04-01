class Médico:
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade
    def __str__(self):
        return f"Médico: {self.nome}, Especialidade: {self.especialidade}"
    
class Paciente:
    def __init__(self, email, dt_nascimento, nome):
        self.email = email
        self.dt_nascimento = dt_nascimento
        self.nome = nome
    def __str__(self):
        return f"Paciente: {self.email}, Data de nascimento: {self.dt_nascimento}"
    
class exame:
    def __init__(self, data_realizado, resultado,dataehora_consulta):
        self.data_realizado = data_realizado
        self.resultado = resultado
        self.dataehora_consulta = dataehora_consulta
    def __str__(self):
        return f"Exame: Data realizado: {self.data_realizado}, Resultado: {self.resultado}, Data e hora da consulta: {self.dataehora_consulta}"
    medico = Médico("Dr. João", "Colesterol")

'''
⣟⣻⢟⣿⠃⠀⠀⠀⠀⠀⠀⡀⢀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠠⠀⠄⠠⠀⠄⠠⢀⠀⢸
⣯⣗⡟⣾⡁⠀⠀⠀⠀⠀⠀⠐⠀⠌⠐⡀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣤⣁⡈⠀⠡⠈⡐⠀⠂⣽
⡷⣮⡽⣳⠅⠀⠀⠀⠀⠀⠀⠀⠈⢀⠂⠄⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠁⢀⠂⠁⠄⡈⠄⣻
⣟⣷⡻⠍⠀⠀⠀⠀⠀⠀⠀⢀⠐⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠟⠛⠋⠉⠉⠀⢀⠠⢀⠂⠄⡈⠐⠠⠐⠀⣿
⣟⣎⠁⠀⢀⠀⠄⠀⠠⠐⢈⣤⠶⠿⠿⠿⠛⠛⠋⠉⡉⠉⠁⠀⣀⣠⣴⠎⠉⣡⠀⠀⠂⠄⠂⡀⠂⠄⢁⠂⢁⠂⣿
⡧⣟⡷⣶⣤⣤⡀⠀⠀⠀⡀⠀⠀⡀⠀⠀⠂⠀⡀⠀⠀⣠⣶⣿⣿⣿⣿⡏⣐⠋⡀⠀⡁⠂⢁⠠⠁⡈⠄⠐⠠⠀⣿
⡷⣟⣷⡹⣶⣹⣗⠀⡀⠀⠀⠀⣄⠁⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣧⣾⡅⠀⠠⠁⠂⠄⠂⠄⡈⠄⠡⠀⣿
⣯⣟⡶⣻⢵⣫⢾⣆⠈⠀⠀⢰⣿⣷⣦⣤⣀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠁⠂⠡⠐⢈⠠⢀⠂⠁⠄⣻
⡷⣯⡗⣯⣻⡵⣛⡾⣻⢦⠀⠘⠋⠉⠸⠿⠿⠷⠈⢻⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣷⡀⠈⠐⡈⠠⢀⠂⠠⠁⠂⣿
⣟⡷⣯⢷⣹⠾⣝⣳⢽⣫⡇⠀⠀⠴⢶⣶⣶⣾⣿⣶⣽⣿⣿⣿⣿⠟⣰⣿⣿⣿⣿⣿⡧⠈⠀⠄⡁⠄⠂⡁⠄⡁⢾
⣯⣟⣧⠿⣼⢫⣟⡼⣳⢯⡗⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣾⣿⣿⣿⣿⣿⣿⣿⣇⠈⠀⠄⢂⠐⠠⠐⠀⣿
⡷⢯⣞⣻⢼⡻⣜⣳⣽⣫⡇⠀⠀⠄⠘⢿⣿⣿⣿⣿⣿⠟⠋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡀⠐⠈⠠⢀⠁⠂⡁⢾
⡷⣾⡹⣏⣞⡳⣟⢯⡽⢯⣷⡀⠀⠀⠄⠈⠛⠛⠛⠋⠉⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠐⠠⢈⠐⠠⠁⣾
⡿⣵⢫⠷⣭⢻⣝⡮⢿⡹⣞⡽⣾⢶⡶⣶⢾⣞⣧⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠡⠀⢂⠁⠄⣿
⣟⡧⣟⢯⣳⣛⣮⡽⣫⣗⢯⣞⡳⢿⣜⣮⠷⡽⣞⣇⠀⠀⠀⠀⠀⠁⠈⣿⣿⣿⣿⣿⣿⣿⣿⣗⡄⠀⢁⠂⢈⠀⣿
⣯⡽⢮⢷⣣⢟⡶⣝⢷⢾⡹⣎⣿⣹⣎⣷⡻⣽⣻⢾⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣷⠈⣄⠀⠀⠂⠀⣻
⣷⡻⣝⣮⢳⣏⢿⡼⣫⣏⢷⣏⣶⢻⡼⣶⣻⠗⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠏⣰⡿⣶⢦⡀⠀⣽
⣷⣻⠼⣎⢷⣚⣧⢟⡽⣞⡧⣟⣼⢻⣞⠗⠁⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡟⢰⣯⢳⣯⢿⠁⠀⣿
⣷⢫⡟⡽⣎⢿⣜⣯⢻⣝⠾⣝⡾⣯⠁⣠⠀⠀⠀⠀⢸⣗⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⠁⣾⡹⢯⣞⡿⠀⡄⣿
⣯⠿⣼⣳⢽⣚⣞⢮⣟⢾⣹⣟⡾⠁⢠⡇⠀⠀⠀⠀⠸⣯⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠃⣼⢯⣽⢳⣯⠁⣼⡇⣿
⣟⡿⡼⣝⢾⣹⢮⡗⣯⢿⣜⡷⡏⠀⣸⠀⠀⠀⡀⣴⠀⣏⣦⠀⠀⠀⠀⠀⠀⠀⢿⣿⢃⣼⣛⡾⣼⡻⠈⠘⢳⡏⣿
⣟⡾⣵⣻⢮⡷⣯⣞⣷⣻⣼⡻⠀⠠⠁⣀⣀⣀⠀⠈⢇⢸⣧⣦⡀⠀⠀⠀⠀⠀⠈⢡⣾⣳⢯⣟⡷⠁⠀⠀⠀⠀⣿

'''