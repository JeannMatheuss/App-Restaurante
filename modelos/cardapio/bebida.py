from modelos.cardapio.item_cardapio import itemCardapio

class Bebida(itemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho