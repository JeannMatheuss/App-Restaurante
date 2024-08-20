class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria) -> None:  # método construtor __init__
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self) -> str:
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(25)}")

    @property
    def ativo(self):
        return '☒' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
