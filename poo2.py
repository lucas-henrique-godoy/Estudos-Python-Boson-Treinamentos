class Veiculo:
    # Método que simula o movimento do veículo
    def movimentar(self):
        print(f'Sou um veículo e me desloco!')

    # Método construtor que inicializa os atributos do veículo
    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante  # Atributo privado para o fabricante do veículo
        self.__modelo = modelo  # Atributo privado para o modelo do veículo
        self.__num_registro = None  # Atributo privado para o número de registro do veículo, inicialmente definido como None

    # Setter para o número de registro
    def set_num_registro(self, registro):
        self.__num_registro = registro  # Atribui o valor recebido ao atributo privado __num_registro

    # Getter para o fabricante e modelo do veículo
    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}.\n')

    # Getter para o número de registro do veículo
    def get_num_de_registro(self):
        return self.__num_registro  # Retorna o valor do atributo privado __num_registro

# Bloco principal do código, executado quando o script é executado diretamente
if __name__ == '__main__':
    meu_veiculo = Veiculo('GM', 'Cadillac Escalade')  # Cria uma instância da classe Veiculo com fabricante 'GM' e modelo 'Cadillac Escalade'
    meu_veiculo.movimentar()  # Chama o método movimentar, que imprime uma mensagem sobre o movimento do veículo
    meu_veiculo.get_fabr_modelo()  # Chama o método get_fabr_modelo, que imprime o modelo e fabricante do veículo
    meu_veiculo.set_num_registro(490321 - 1)  # Define o número de registro do veículo usando o setter (490321 - 1 é avaliado como 490320)
    print(f'Registro: {meu_veiculo.get_num_de_registro()}\n')  # Imprime o número de registro do veículo usando o getter
