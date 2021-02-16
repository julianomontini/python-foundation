class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def dizer_nome(self):
        return self.nome

class Cidadao:
    def __init__(self, cpf):
        self.cpf = cpf

class Funcionario(Pessoa, Cidadao):
    def __init__(self, nome, matricula, cpf):
        Pessoa.__init__(self, nome)
        Cidadao.__init__(self, cpf)
        self.matricula = matricula
    def falar_matricula(self):
        return self.matricula

arr_pessoas = [
    Pessoa('P1'),
    Pessoa('P2'),
    Funcionario('P3', '123', '123'),
    Funcionario('P4', '456', '456')
]

for pessoa in arr_pessoas:
    print(pessoa.dizer_nome())