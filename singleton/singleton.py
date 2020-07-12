class Singleton:
    _instance = None

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @staticmethod
    def get_instance():
        if not Singleton._instance:
            Singleton._instance = Singleton()
        return Singleton._instance


if __name__ == '__main__':
    obj1 = Singleton.get_instance()
    obj1.nome = 'Luiz'
    print(f'nome obj1: {obj1.nome}')

    obj2 = Singleton.get_instance()
    print(f'nome obj2: {obj2.nome}')
