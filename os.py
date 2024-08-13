# Módulo os(OPERATE SYSTEM): Muito empregado a realização de funções relacionadas a sistemas de arquivos, arquivos em geral, diretórios, e outras funcionalidades de sistema operacional. Podemos fazer uma série de tarefas relacionadas a arquivos, diretórios e pastas, etc. Para usar o módulos devemos seguir os seguintes passos:
# 1 - Abrir o terminal,
# 2- Digitar py no terminal para entrar no interpretador interativo do python,
# 3- Importar o módulo os digitando: import os.
# EXEMPLOS:

# os.name -> Retorna uma string relacionada ao tipo do sistema operacional se for Windows retorna'nt', e se for MAC ou Linux retorna 'posix'.

# os.getcwd() -> Retorna qual o diretório atual em que o código esta aberto.

# os.curdir -> É um atalho. Retorna um ponto '.' , que siginifica um atalho para o diretório atual, quando eu quiser realizar algum tipo de tarefa que faça referencia direta ao diretorio atual(aberto), eu posso utilizar o ponto ou escrever os.curdir(mais indicado pois o próprio pytohn gerencia isso.)

# os.listdir() -> Visualizar o conteúdo do diretorio atual. 

# os.listdir('c:\\') -> Visualizar o conteúdo de outro diretorio que não seja o diretório atual. (Neste caso visualizando o que tem na raiz do meu sistema). 

# os.chdir('c:\\') -> Mudar de diretório, pode ser um absoluto(desde a raiz ate a pasta desejada) ou relativo(a partir do diretório atual, entre em uma outra pasta). (Neste exemplo mudou para o diretório raiz do drive C: em sistemas Windows, se quiser ver o diretorio atual é so usar os.getcwd e vera que que esta na raiz).

# os.path.join() junta dois ou mais pedaços de um caminho de arquivo. Monta" ou "constrói" um caminho de arquivo. Essa expressão é apropriada porque a função combina várias partes de um caminho em um único caminho completo, utilizando o separador de diretórios correto para o sistema operacional.

# os.mkdir('Teste') -> Cria uma pasta.(Neste exemplo nós criamos uma pasta chamada Teste no diretorio raiz do drive C:)

# os.rename('c:\\Teste3', 'c:\\Teste10') -> Renomeia uma pasta. Neste exemplo muda o nome da pasta de TESTE2 para Teste10. Obs: Se eu ja estivesse dentro do c:, ou seja, se ele fosse o diretório atual em que eu estivesse,  era so usar os.rename('Teste3', 'Teste10').

# os.rmdir(caminho da pasta)  Remove um diretório se estiver vazio.

# os.remove() -> Remove um arquivo.

# os.path.basename(path) -> Retorna o nome base do caminho fornecido, que pode ser um arquivo ou diretório.
#print(os.path.basename('C:\\Users\\SeuUsuario\\Documents\\arquivo.txt'))  # Saída: 'arquivo.txt'

# os.path.basename(os.getcwd()) -> Retorna o nome base do diretório de trabalho atual, que é o nome do diretório onde o script está sendo executado.
#print(os.path.basename(os.getcwd()))

# os.path.dirname(path) -> Retorna o caminho do diretório pai do caminho fornecido.
# Quando usado com os.getcwd(), retorna o diretório pai do diretório de trabalho atual.
#print(os.path.dirname(os.getcwd()))

#  os.makedirs() Criar diretórios de forma recursiva(criar varios diretórios de uma vez, um dentro do outro):

# os.path.exists(caminho) -> Verificar se um caminho existe ou não. Retorna um booleano.
# os.path.isdir() -> Verificar se um item é um diretório.
# os.path.isfile() -> Verficar se um item é um arquivo.
# os.path.splitext()-> Obter o nome de um arquivo e separa da sua extensão.


# EXEMPLO DE USO 1 -> Criar pastas fora do diretório atual, especificamente em um diretório diferente

#import os  # Importa o módulo os, que fornece funções para interagir com o sistema operacional

# Define o nome da nova pasta que será criada
#pasta_nova = 'Teste3'

# Define o caminho da pasta pai onde a nova pasta será criada
#pasta_pai = 'c:\\'

# Cria o caminho completo para a nova pasta, combinando o caminho da pasta pai com o nome da nova pasta
#caminho_completo = os.path.join(pasta_pai, pasta_nova)

# Exibe o caminho completo da nova pasta para confirmação
#print(caminho_completo)

# Cria a nova pasta no caminho especificado
#os.mkdir(caminho_completo)

# Lista o conteúdo do diretório atual (sem parâmetros, lista o diretório atual onde o script está sendo executado)
#print(os.listdir())  # Este comando mostra o conteúdo do diretório de trabalho atual, não do diretório especificado

# Lista o conteúdo do diretório 'c:\\' para verificar a presença da nova pasta criada
#print(os.listdir('c:\\'))

# EXEMPLO DE USO 2 -> O código cria um arquivo, lista os arquivos do diretório atual, extrai e exibe o nome e a extensão do arquivo recém-criado.

#import os  # Importa o módulo 'os' para interação com o sistema operacional

# Criação de um novo arquivo. O modo 'x' cria o arquivo somente se ele não existir, caso contrário, gera uma exceção.
#manipulador = open('arq.txt', 'x')
#manipulador.close()  # Fecha o arquivo após a criação para liberar recursos.

# Lista os arquivos e diretórios no diretório atual.
# Isso mostra todos os arquivos e pastas presentes no diretório onde o script está sendo executado.
#print(os.listdir())
# Saída esperada: ['.git', '.gitattributes', 'aleatorios.py', ..., 'arq.txt', ...]

# Obtém o nome base do arquivo a partir de um caminho completo.
# Aqui, 'os.path.basename' extrai o nome do arquivo do caminho completo fornecido.
#arquivo = os.path.basename('C:\\Users\\lucasgodoy\\Desktop\\Estudos-Python-Boson-Treinamentos\\arq.txt')

# Exibe o nome do arquivo extraído.
#print(arquivo)  # Saída esperada: 'arq.txt'

# Divide o nome do arquivo em duas partes: nome e extensão.
# 'os.path.splitext' separa o nome do arquivo da sua extensão.
# Retorna uma tupla onde o primeiro elemento é o nome do arquivo e o segundo é a extensão.
#print(os.path.splitext(arquivo))
# Saída esperada: ('arq', '.txt')

#_______________________________________________________________________________________________________________________

# BIBLIOTECA PATHLIB: é uma biblioteca padrão do Python que fornece uma maneira orientada a objetos para manipulação de caminhos de arquivos e diretórios.
# EXEMPLOS DE USOS:

#EX01:
# Importa a biblioteca pathlib para manipulação de caminhos
#import pathlib

# Cria um objeto Path representando o diretório atual
#caminho = pathlib.Path()

# Obtém e exibe o diretório de trabalho atual
#print(caminho.cwd())  # Output esperado: o caminho completo do diretório atual

#EX02:


# BIBLIOTECA SHUTIL:  um módulo padrão do Python que oferece uma coleção de funções para manipulação de arquivos e operações relacionadas a arquivos e diretórios. Ele fornece funcionalidades para copiar, mover e deletar arquivos e diretórios, além de outras operações úteis.





