# Sistema de Gestão de Restaurantes

Este projeto implementa um sistema simples para gerenciar restaurantes e suas avaliações. Os usuários podem registrar restaurantes, alternar seu estado (ativo ou inativo) e registrar avaliações para cada estabelecimento. Além disso, é possível listar todos os restaurantes cadastrados com detalhes como nome, categoria, média de avaliações e status.

## Estrutura do Projeto

O código está organizado em duas classes principais:

### 1. Classe `Restaurante`
Representa um restaurante e contém os seguintes atributos e métodos:

- **Atributos:**
  - `_nome`: Nome do restaurante.
  - `_categoria`: Categoria do restaurante (e.g., Gourmet, Fast Food).
  - `_ativo`: Indica se o restaurante está ativo ou inativo.
  - `_avaliacao`: Lista que armazena as avaliações recebidas.

- **Métodos:**
  - `__init__(self, nome, categoria)`: Inicializa os atributos do restaurante.
  - `__str__(self)`: Retorna uma string formatada com o nome e a categoria do restaurante.
  - `listar_restaurantes(cls)`: Método de classe que lista todos os restaurantes cadastrados com suas respectivas informações.
  - `ativo(self)`: Retorna o status do restaurante como "⌧" para ativo e "☐" para inativo.
  - `alternar_estado(self)`: Alterna o estado do restaurante entre ativo e inativo.
  - `receber_avaliacao(self, cliente, nota)`: Registra uma nova avaliação para o restaurante, desde que a nota esteja entre 1 e 5.
  - `media_avaliacoes(self)`: Calcula e retorna a média das avaliações recebidas.

### 2. Classe `Avaliacao`
Representa uma avaliação feita por um cliente e contém os seguintes atributos:

- **Atributos:**
  - `_cliente`: Nome do cliente que fez a avaliação.
  - `_nota`: Nota dada pelo cliente (entre 1 e 5).

## Como Utilizar

### Pré-requisitos

Certifique-se de que você tem Python instalado em sua máquina.

### Execução

1. Clone este repositório para o seu ambiente local.
2. Navegue até o diretório do projeto.
3. Execute o arquivo principal:

```bash
python main.py

from modelos.restaurante import Restaurante

# Criando um restaurante
restaurante_praca = Restaurante('praça', 'Gourmet')

# Recebendo avaliações
restaurante_praca.receber_avaliacao('Gui', 4)
restaurante_praca.receber_avaliacao('Lais', 3)
restaurante_praca.receber_avaliacao('Emy', 5)

# Listando restaurantes
Restaurante.listar_restaurantes()

Nome do restaurante          | Categoria                  | Avaliação                  | Status
Praça                        | GOURMET                    | 4.0                        | ☐

