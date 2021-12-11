#Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá
#uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

palavra = 'excelentissimo'.upper() #O uso das aspas é importante para que não seja compreendida como variável, e sim como string
erros = 0

print("JOGO DA FORCA! Você tem 6 chances de erros")
print()
print("A palavra é: ", end='')
for letra in palavra: #letra é variável que guarda cada caractere extraido no for. Para letra dentro de palavra
    print('_ ', end='') #Ao invés de colocar as letras, vamos colocar os espaços correspondente ao número de palavras _

conjunto_letras_palavra = set(palavra)  # gera o conjunto a partir da variável palavra
conjunto_letras_digitadas = set()
# print('X' in conjunto_letras_palavra) #comando que verifica se um determinado elemento está dentro de conjunto
# print(conjunto_letras_palavra.issubset(conjunto_letras_digitadas)) verifica se o 1ª está contido no segundo
# print(conjunto_letras_digitadas.issubset(conjunto_letras_palavra))

while not conjunto_letras_palavra.issubset(conjunto_letras_digitadas) and erros < 6:
    print()
    letra_digitada = input("Digite uma letra para forca: ").upper()
    conjunto_letras_digitadas.add(letra_digitada) #adicionei o valor de letra_digitada ao conjunto
    if letra_digitada in conjunto_letras_palavra:
        print('A palavra é: ' , end='')
        for letra in palavra:
            if letra in conjunto_letras_digitadas:
                print(f'{letra} ', end ='')
            else:
                print('_ ', end='') #essa parte faz que as condições não cumpridas continuem como _
    else:
        erros += 1
        print (f"Você ainda tem {(erros+(-6))*-1} chances para errar!")
    print()
    print('Letras já digitadas: ', conjunto_letras_digitadas)
if erros < 6:
    print("GANHOU")
else:
    print("perdeu...")