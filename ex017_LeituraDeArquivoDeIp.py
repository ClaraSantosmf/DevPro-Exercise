#Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo,
# contendo um relatório dos endereços IP válidos e inválidos.
# O arquivo de entrada possui o seguinte formato:
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 257.32.4.5
# 85.345.1.2
# 1.2.3.4
# 9.8.234.5
# 9.8.234
# 192.168.0.256
# O arquivo de saída possui o seguinte formato:
# [Endereços válidos:]
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 1.2.3.4
# [Endereços inválidos:]
# 257.32.4.5
# 85.345.1.2
# 9.8.234.5
# 9.8.234
# 192.168.0.256

def validar (ip:str) -> bool: #função que indicará se o endereço de IP é válido ou não, por dois passos
    numeros = ip.split('.') #split com o parâmetro ponto separa os trechos de uma variável

    if len(numeros) != 4: # verificar se as strings possuem 4 números na string
        return False

    for n in numeros:
        if not (0<= int(n) <= 255): #verifica se o inteiro (revertido por int(n)) está entre 0 a 255.
            return False

    return True #se passar pelas duas validações, o retorno é verdadeiro
ips_validos =[] #lista vazia para organizar os ips válidos
ips_invalidos =[] #lista vazia para organizar os ips inválidos

#A palavra with open abre o arquivo, indicando 1º o nome da pasta/nome do arquivo, lendo-o no contexto do programa
with open('ips.txt', 'r') as arquivo: # o 'r' informa qual modo que haverá interação com o arquivo, as arquivo significa atribuir uma variável de representação a ele.
    for linha in arquivo:                        # assim como acesso de uma lista ou letras de uma string, é possível acessar linhas dos arquivos
        ip=linha.strip()                         #método strip retira os tabs e espaços iniciais e finais, retirando o carácter especial \n.
        if validar(ip):
            ips_validos.append(ip)                   #o append acrescerá os IPs com retorn bool true
        else:
            ips_invalidos.append(ip)                 # o append acrescerá os IPs com retorn bool false
        print(ip, validar(ip))                   # Nessa linha, então poderá imprimir tanto o IP do arquivo, quanto o resultado dele elaborado na função validar

#Para escrever o arquivo com o W, assim como vai interagir com o arquivo pelo as arquivo
with open('ips_saida.txt', 'w') as arquivo:
    arquivo.writelines('[Endereços Válidos:]\n') #escrevendo dentro do arquivo cabeçalho com 'endereços válidos'

    for ip in ips_validos: #para IPs_válidos dentro de IP, escreva no arquivo
        arquivo.writelines(f'{ip}\n')

    arquivo.writelines('[Endereços Válidos:]\n') #escrevendo dentro do arquivo cabeçalho com 'endereços inválidos'
    for ip in ips_invalidos:
        arquivo.writelines(f'{ip}\n')