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

func = Funcionario('Juliano', '123', '456')
print(func.nome)
print(func.matricula)
print(func.cpf)