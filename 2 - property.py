class Pessoa:

    especie = 'Homo Sapiens'

    def __init__(self, primeiro_nome, ultimo_nome):
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome

    @property
    def nome_completo(self):
        return self.primeiro_nome + ' ' + self.ultimo_nome

    @classmethod
    def mudar_especie(cls, especie):
        cls.especie = especie

# p = Pessoa('Juliano', 'Montini')
# print(p.nome_completo)

p = Pessoa('Juliano', 'Montini')
p2 = Pessoa('Joao', 'Silva')
Pessoa.mudar_especie('Indefinido')
print(p2.especie)