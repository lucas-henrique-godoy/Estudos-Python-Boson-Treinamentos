# Orientação a Objetos: Paradigma de Programação(estilo/forma de programar).
# Classes e Objetos
# Classes: São modelos abstratos que vão representar itens do mundo real dentro do software.
# Objetos: Sao as ocorrências dessas classes, são essas classes carregadas na memória efetivamente existindo pra valer.

# SINTAXE CLASSE:
    # Atributos: São propriedades das classes similares a variaveis, ou seja, estrutura que guardam valores.
    # Métodos: São as funcionalidades ou ações que classe pode realizar ou sofrer(são similares a funções). Ou seja, uma função dentro de uma classe se chama método.
    # Instanciar: Significa tornar a classe que é um modelo, real na memória do computador.
#_______________________________________________________________________________________________________________________________________________________________________

class Veiculo:
    # Método que simula o movimento do veículo
    def movimentar(self):
        print(f'Sou um veículo e me desloco!')

    # Método construtor que inicializa os atributos do veículo
    def __init__(self, fabricante, modelo): # __INIT__: É O CONSTRUTOR QUE INICIALIZA A CLASSE
        self.__fabricante = fabricante # Atribui o valor de 'fabricante' ao atributo privado '__fabricante' da instância
        self.__modelo = modelo # Atributo privado para o modelo do veículo
        self.__num_registro = None # Atributo privado para o número de registro do veículo, inicialmente definido como None


    # Setter para o número de registro.   -> Setter: É um método que permite gravar um dado dentro do objeto.
    def set_num_registro(self, registro):
        self.__num_registro = registro # Atribui o valor recebido ao atributo privado __num_registro

    # Getter para o fabricante e modelo do veículo -> Getter: É um método especial(função) que permite acessar os atributos de dentro da classe ou acessar outros elementos dentro da classe.
    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}.\n')

    # Getter para o número de registro do veículo
    def get_num_de_registro(self):
        return self.__num_registro  # Retorna o valor do atributo privado __num_registro
        
class Carro(Veiculo):
    # Método __init__ será herdado
    def movimentar(self):
       print(f'Sou um carro e ando pelas ruas!') 

class Motocicleta(Veiculo):
    def movimentar(self):
        print(f'Corro muito!')






# Bloco principal do código, executado quando o script é executado diretamente
if __name__ == '__main__':
    meu_veiculo = Veiculo('GM', 'Cadillac Escalade')  # Cria uma instância da classe Veiculo com fabricante 'GM' e modelo 'Cadillac Escalade'
    meu_veiculo.movimentar()  # Chama o método movimentar, que imprime uma mensagem sobre o movimento do veículo
    meu_veiculo.get_fabr_modelo()  # Chama o método get_fabr_modelo, que imprime o modelo e fabricante do veículo
    meu_veiculo.set_num_registro('490321 - 1')  # Define o número de registro do veículo usando o setter (490321 - 1 é avaliado como 490320)
    print(f'Registro: {meu_veiculo.get_num_de_registro()}\n')  # Imprime o número de registro do veículo usando o getter

    meu_carro = Carro('Volkswagen', 'Polo')
    meu_carro.movimentar()
    meu_carro.get_fabr_modelo()

    seu_carro = Carro('Audi', 'A5 Sportback ')
    seu_carro.movimentar()
    seu_carro.get_fabr_modelo()



# OBS: Acessar atributos internos utilizando métodos é vantajoso pois é possivel programar esse método, de forma que os dados sejam acessíveis somente da forma que eu desejo, preservando assim a integridade desses dados. Recomendado por Fábio da Bóson Treinamentos, sempre utilizar atributos privados com __ e criar métodos getter para acessar esses atributos dentro de uma classe. 
# USAMOS SETTER PARA GRAVAR O VALOR E O GETTER PARA OBTER O VALOR(fazer a leitura).     
# O self é o que vai diferenciar um obejeto do outro
