# Manipulação de arquivos de texto.

# LEITURA DE ARQUIVOS

# Comentado, mas mostra como usar o método read() para ler todo o conteúdo de um arquivo de uma vez.
# print(f'\nMétodo read():\n')
# print(manipulador.read())

# Comentado, mas mostra como usar o método readline() para ler uma linha de cada vez.
# print(f'\nMétodo readline():\n')
# print(manipulador.readline())  # Lê a primeira linha do arquivo
# print(manipulador.readline())  # Lê a segunda linha do arquivo

# Comentado, mas mostra como usar o método readlines() para ler todas as linhas do arquivo e retorná-las como uma lista.
# print(f'\nMétodo readlines():\n')
# print(manipulador.readlines())

# Abre o arquivo 'arquivo.txt' no modo de leitura ('r') e com codificação UTF-8.
# Lê o arquivo linha por linha, remove espaços em branco no final de cada linha, e imprime a linha.
# Se ocorrer um erro ao abrir o arquivo, imprime uma mensagem de erro.
try:
    manipulador = open('arquivo.txt', 'r', encoding='utf-8')
    for linha in manipulador:
        linha = linha.rstrip()  # Remove espaços em branco do final da linha
        print(linha)
except IOError:
    print(f'Não foi possível abrir o arquivo')  # Mensagem de erro se o arquivo não puder ser aberto
else:
    manipulador.close()  # Fecha o arquivo após a leitura

# Abre o arquivo 'arquivo2.txt' em um diretório específico para leitura.
# Lê o arquivo linha por linha, remove espaços em branco no final de cada linha, e imprime a linha.
# Se ocorrer um erro ao abrir o arquivo, imprime uma mensagem de erro.
try:
    manipulador = open('C:\\Users\\lucas\\OneDrive\\Documentos\\arquivo2.txt', 'r', encoding='utf-8')
    for linha in manipulador:
        linha = linha.rstrip()  # Remove espaços em branco do final da linha
        print(linha)
except IOError:
    print(f'Não foi possível abrir o arquivo')  # Mensagem de erro se o arquivo não puder ser aberto
else:
    manipulador.close()  # Fecha o arquivo após a leitura

# Solicita ao usuário um termo para buscar dentro do arquivo 'arquivo.txt'.
# Abre o arquivo em modo de leitura e busca o termo fornecido pelo usuário em cada linha.
# Se o termo for encontrado, imprime a linha correspondente; caso contrário, informa que o termo não foi encontrado.
try:
    texto = input(f'Qual termo deseja procurar no arquivo? ')
    manipulador = open('arquivo.txt', 'r', encoding='utf-8')
    for linha in manipulador:
        linha = linha.rstrip()  # Remove espaços em branco do final da linha
        if texto in linha:
            print(f'A string foi encontrada!')
            print(linha)
        else:
            print(f'String não foi encontrada!')
except IOError:
    print(f'Não foi possível abrir o arquivo')  # Mensagem de erro se o arquivo não puder ser aberto
else:
    manipulador.close()  # Fecha o arquivo após a leitura

# ESCRITA EM ARQUIVOS DE TEXTO:

# EX01- Escrevendo e substituindo texto:
# Abre o arquivo 'arquivo.txt' no modo de escrita ('w'). Isso cria um novo arquivo ou sobrescreve um existente.
# Escreve duas linhas de texto no arquivo.
try:
    manipulador = open('arquivo.txt', 'w', encoding='utf-8')
    manipulador.write('Bóson Treinamentos\n')
    manipulador.write('Como criar um arquivo de texto com Python.')
except IOError:
    print(f'Não foi possível abrir o arquivo')  # Mensagem de erro se o arquivo não puder ser aberto
else:
    manipulador.close()  # Fecha o arquivo após a escrita

# EX02- Escrevendo e Acrescentando texto:
# Abre o arquivo 'arquivo.txt' no modo de acrescentar ('a'). Isso adiciona texto ao final do arquivo existente.
# Adiciona duas novas linhas de texto ao final do arquivo.
try:
    manipulador = open('arquivo.txt', 'a', encoding='utf-8')
    manipulador.write('\nPython é muito empregado em IA.')
    manipulador.write('\nInteligência Artificial veio para ficar!')
except IOError:
    print(f'Não foi possível abrir o arquivo')  # Mensagem de erro se o arquivo não puder ser aberto
else:
    manipulador.close()  # Fecha o arquivo após a escrita

# EX03- Escrevendo em um arquivo de texto usando variáveis:
# Define uma string em uma variável e abre o arquivo 'arquivo.txt' no modo de acrescentar ('a').
# Adiciona o conteúdo da variável ao final do arquivo.
texto = '\nPython é usado em Ciência de Dados extensivamente'
try:
    manipulador = open('arquivo.txt', 'a', encoding='utf-8')
    manipulador.write(texto)
except IOError:
    print(f'Não foi possível abrir o arquivo')  # Mensagem de erro se o arquivo não puder ser aberto
else:
    manipulador.close()  # Fecha o arquivo após a escrita

# EX04- ESCRITURA DOS ITENS DE UMA LISTA EM UM ARQUIVO DE TEXTO:
# Define uma lista de frutas e abre um novo arquivo 'frutas.dat' no modo de escrita ('w').
# Escreve cada item da lista no arquivo, um por linha.
# Após a escrita, abre o arquivo novamente para leitura e imprime seu conteúdo.
frutas = ['Morango\n', 'Uva\n', 'Caju\n', 'Amora\n', 'Framboesa\n', 'Graviola']

# Criar e gravar o arquivo com itens da lista
try:
    manipulador = open('frutas.dat', 'w', encoding='utf-8')
    manipulador.writelines(frutas)  # Escreve todos os itens da lista no arquivo
except IOError:
    print(f'Não foi possível abrir o arquivo')  # Mensagem de erro se o arquivo não puder ser aberto
else:
    manipulador.close()  # Fecha o arquivo após a escrita

# Ler o arquivo criado
try:
    manipulador = open('frutas.dat', 'r', encoding='utf-8')
    print(manipulador.read())  # Lê e imprime o conteúdo do arquivo
except IOError:
    print(f'Não foi possível abrir o arquivo')  # Mensagem de erro se o arquivo não puder ser aberto
else:
    manipulador.close()  # Fecha o arquivo após a leitura
