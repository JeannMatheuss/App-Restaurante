class Restaurante:
    def __init__(self, nome, categoria) -> None:  # método construtor __init__
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza express', 'Italiana')

restaurantes = [restaurante_praca, restaurante_pizza]

print(vars(restaurante_praca))
print(vars(restaurante_pizza))