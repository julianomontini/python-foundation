class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar_nome(self):
        print('Meu nome é ' + self.nome)

p1 = Pessoa('Juliano', 25)
p2 = p1

p2.nome = 'Joao'
print(p1.nome)