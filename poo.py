# Orientação a Objetos: Paradigma de Programação(estilo/forma de programar).
# Classes e Objetos
# Classes: São modelos abstratos que vão representar itens do mundo real dentro do software.
# Obejetos: Sao as ocorrências dessas classes, são essas classes carregadas na memória efetivamente existindo pra valer.

# SINTAXE CLASSE:
    # Atributos: São propriedades das classes similares a variaveis, ou seja, estrutura que guardam valores.
    # Métodos: São as funcionalidades ou ações que classe pode realizar ou sofrer(são similares a funções). Ou seja, uma função dentro de uma classe se chama método.
    # Instanciar: Significa tornar a classe que é um modelo, real na memória do computador.
class Veiculo:
    def movimentar(self):
        print(f'Sou um veículo e me desloco!')

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None


    # Setter: É um método que permite gravar um dado dentro do objeto.
    # Getter: É um método especial(função) que permite acessar os atributos de dentro da classe ou acessar outros elementos dentro da classe.
    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}.\n')
        


if __name__ == '__main__':
    meu_veiculo = Veiculo('GM', 'Cadillac Escalade')
    meu_veiculo.movimentar()
    meu_veiculo.get_fabr_modelo()

    



    
     

