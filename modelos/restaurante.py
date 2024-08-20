class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria) -> None:  # método construtor __init__
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self) -> str:
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}")

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza express', 'Italiana')

Restaurante.listar_restaurantes()