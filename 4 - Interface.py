import abc

class AbstractRepository(abc.ABC):
    def print_hi(self):
        print('hi')

    @abc.abstractmethod
    def get(self, id):
        pass

    @abc.abstractmethod
    def save(self, any):
        pass

class FileRepository(AbstractRepository):
    def get(self, id):
        print('got ' + id)

    def save(self, any):
        print('saved ' + any)

fr = FileRepository()
fr.get('1')
fr.save('1')
fr.print_hi()