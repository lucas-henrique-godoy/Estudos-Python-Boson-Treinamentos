# Orientação a Objetos:
# - Paradigma de programação que utiliza classes e objetos.
# - Classes: Modelos que representam entidades do mundo real.
# - Objetos: Instâncias concretas das classes, existentes na memória.

# Estrutura de uma Classe:
# - Atributos: Propriedades que armazenam dados.
# - Métodos: Funções dentro da classe que definem ações.
# - Instanciar: Criar um objeto da classe na memória.

class Veiculo:
    # Método que simula o movimento do veículo
    def movimentar(self):
        print('Sou um veículo e me desloco!')

    # Construtor que inicializa atributos
    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante  # Atributo privado para o fabricante
        self.__modelo = modelo          # Atributo privado para o modelo
        self.__num_registro = None      # Atributo privado para o número de registro

    # Setter para o número de registro
    def set_num_registro(self, registro):
        self.__num_registro = registro  # Define o número de registro

    # Getter para fabricante e modelo
    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}.')

    # Getter para o número de registro
    def get_num_de_registro(self):
        return self.__num_registro  # Retorna o número de registro

# Herança:
# - Carro herda de Veiculo, adquirindo seus atributos e métodos.
class Carro(Veiculo):
    # Sobrescreve o método movimentar para uma implementação específica
    def movimentar(self):
        print('Sou um carro e ando pelas ruas!')

class Motocicleta(Veiculo):
    # Sobrescreve o método movimentar para uma implementação específica
    def movimentar(self):
        print('Corro muito!')

class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria  # Novo atributo específico para Avião
        super().__init__(fabricante, modelo)  # Chama o construtor da classe base
    
    def get_categoria(self):
        return self.__cat  # Retorna a categoria do avião
    
    # Sobrescreve o método movimentar para uma implementação específica
    def movimentar(self):
        print('Eu voo alto!')

# Bloco principal do código
if __name__ == '__main__':
    meu_veiculo = Veiculo('GM', 'Cadillac Escalade')  # Cria um objeto da classe Veiculo
    meu_veiculo.movimentar()  # Chama o método movimentar do Veiculo
    meu_veiculo.get_fabr_modelo()  # Mostra modelo e fabricante
    meu_veiculo.set_num_registro('490321 - 1')  # Define o número de registro
    print(f'Registro: {meu_veiculo.get_num_de_registro()}')  # Mostra o número de registro

    meu_carro = Carro('Volkswagen', 'Polo')  # Cria um objeto da classe Carro
    meu_carro.movimentar()  # Chama o método movimentar do Carro
    meu_carro.get_fabr_modelo()  # Mostra modelo e fabricante do Carro

    seu_carro = Carro('Audi', 'A5 Sportback')  # Cria outro objeto da classe Carro
    seu_carro.movimentar()  # Chama o método movimentar do Carro
    seu_carro.get_fabr_modelo()  # Mostra modelo e fabricante do Carro

    moto = Motocicleta('Harley-Davidson', 'Nightster Special')  # Cria um objeto da classe Motocicleta
    moto.movimentar()  # Chama o método movimentar da Motocicleta
    moto.get_fabr_modelo()  # Mostra modelo e fabricante da Motocicleta

    meu_aviao = Aviao('Boeing', '747', 'Comercial')  # Cria um objeto da classe Aviao
    meu_aviao.movimentar()  # Chama o método movimentar do Aviao
    meu_aviao.get_fabr_modelo()  # Mostra modelo e fabricante do Aviao
    print(f'Categoria: {meu_aviao.get_categoria()}')  # Mostra a categoria do Aviao

# Observações:
# Encapsulamento:
# - Atributos privados (com __) protegem dados e são acessados via métodos (getters e setters).
# - Getters obtêm valores, setters definem valores.

# Herança:
# - Carro e Motocicleta herdam de Veiculo e podem extender ou modificar seus comportamentos.
# - Exemplo: Carro e Motocicleta redefinem o método movimentar.

# Polimorfismo:
# - Permite que métodos com o mesmo nome (movimentar) tenham comportamentos diferentes em classes diferentes.
# - Exemplo: movimentar é implementado de forma distinta em Veiculo, Carro, Motocicleta e Aviao.

# 'self' refere-se à instância atual da classe e é usado para acessar atributos e métodos da instância.
