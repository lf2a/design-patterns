"""Exemplo: Usar uma cafeteira feita nos EUA, para fazer café usando uma tomada de estilo europeu."""


class TomadaEuropeu:
    """ Interface """

    def voltage(self):
        pass

    def live(self):
        pass

    def neutral(self):
        pass

    def earth(self):
        pass


class Tomada(TomadaEuropeu):
    """ Adaptee """

    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0


class USATomada:
    """ Interface """

    def voltage(self):
        pass

    def live(self):
        pass

    def neutral(self):
        pass


class Adapter(USATomada):
    _socket = None

    def __init__(self, socket):
        self._socket = socket

    def voltage(self):
        return 110

    def live(self):
        return self._socket.live()

    def neutral(self):
        return self._socket.neutral()


class CafeteiraEletrica:
    _power = None

    def __init__(self, power):
        self._power = power

    def ferver(self):
        if self._power.voltage() >= 110:
            print("Cafeteira funcionando!")
        else:
            if self._power.live() == 1 and self._power.neutral() == -1:
                print("Hora do café!")
            else:
                print("Sem energia!")


if __name__ == '__main__':
    tomada = Tomada()
    adapter = Adapter(tomada)
    cafeteira = CafeteiraEletrica(adapter)

    cafeteira.ferver()  # fazendo café
