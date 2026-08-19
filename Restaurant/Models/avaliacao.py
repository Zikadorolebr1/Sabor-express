from models.restaurante import Restaurante


class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente
        # Usando o _ para deixar privado
        self._nota = nota
