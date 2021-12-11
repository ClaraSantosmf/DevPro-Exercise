# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
# Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e
# identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o
# seguinte arquivo, chamado "usuarios.txt": Neste arquivo, o nome do usuário possui 15 caracteres.
# A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários,
# de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco,
# de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal.
# O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal

lista_de_dados = []  # espaço para guardar os dados de usuário e linha


# ?? como um parametro passado para a DEF é variável ainda não definida que vai ser utilizada novamente na conta? Estamos falando de linha[16:]?
def transformar_em_megab(tamanho_em_bytes: str) -> float:  # função para transformar bytes em megabytes, com o typerints, dicas de typo (str)
    return int(tamanho_em_bytes) / (2 ** 10) ** 2  # 2 elevado a décida é tranformação em kbytes, e para megabytes, eleva o resultado a 2


with open('usuario.txt', 'r') as arquivo:  # comando para abrir e 'r' ler o arquivo
    for linha in arquivo:  # ler cada linha do arquivo
        linha = linha.strip()  # retira as arestas
        usuario = linha[:15]  # atribuimos ao usuário os 15 primeiros caracteres, correspondendo ao nome utiliando o slice de índice zero até décimo quinto valor
        tamanho_em_disco = transformar_em_megab((linha[16:]))  # para atribuir o número, o resultado da função de transformação a partir do slice de linha no indice 16,
        lista_de_dados.append((usuario, tamanho_em_disco))  # guardamos os valores em uma tupla criada como lista de dados

# construção do relatório escrevendo no arquivo
# variável que guarda as escritas do cabecalho, o que facilita não escrever dentro do bloco with

cabecalho = '''ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.    Usuário        Espaço utilizado     % do uso
'''

with open('relatório.txt', 'w') as arquivo:
    tamanho_total_consumido = sum([tamanho for _, tamanho in lista_de_dados]) #produz uma lista nova com a soma dos valores
    arquivo.writelines(cabecalho)
    for i, dados in enumerate(lista_de_dados, start=1): #enumerate proporcionará dois elementos, nesse caso, o indice e os dados, que devem ser desempacotados
        usuario, tamanho_em_disco = dados   #empacotando
        arquivo.writelines(f'{i:<4}    {usuario} {tamanho_em_disco:9.2f}MB '
                           f'           {tamanho_em_disco/tamanho_total_consumido:6.2%}\n')

#{i} vai inserir o indice começando de zero, por isso é importante colocar start na lista de dados com 1 para orientar o enumerate
#para organizar a quantidade de espaços que devem ser utilizados, e assim entabular os espaços, é usado a notação com :4 para indice
#com alinhamento a esquerda usando o sinal de menor <
#Para formar tamanho em disco é preciso limitar o tamanho de casa decimais com :.2f, dois indica o número de casa décimais e f da o formato de float
#sendo o 9 próprio para espaços que precisamos para manter o alinhamento centralizado
#{tamanho_em_disco/tamanho_total_consumido:.2%}%\n') foi preciso dividir o tamanho de cada um, dividido pelo total e x 100, mas indicado por %.