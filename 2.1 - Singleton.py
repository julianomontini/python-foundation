class ConexaoBanco:

    conexao = None

    @classmethod
    def get_conexao(cls):
        if cls.conexao is None:
            print('Abrindo conexao')
            cls.conexao = 'Conexao aberta'
        return cls.conexao

print(ConexaoBanco.get_conexao())
print(ConexaoBanco.get_conexao())