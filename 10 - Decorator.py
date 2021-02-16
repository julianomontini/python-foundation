def auto_print(func):
    def wrapper(*args, **kwargs):
        print('Entrou')
        print(kwargs)
        func(*args, **kwargs)
        print('Saiu')
    return wrapper


@auto_print
def meu_metodo(value):
    print('Meu metodo ' + value)

meu_metodo(value='abc')