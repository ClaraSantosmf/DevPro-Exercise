#Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados
#quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça
#Mostre a quantidade de valores que foram lidos;
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#Calcule e mostre a soma dos valores;
#Calcule e mostre a média dos valores;
#Calcule e mostre a quantidade de valores acima da média calculada;
#Calcule e mostre a quantidade de valores abaixo de sete;
#Encerre o programa com uma mensagem;
# Primeira tentativa com erros constantes
# lista = []
# lista1 = []
# notas = ()
# soma = 1
# tamanho = len(notas)
#
# while notas != -1:
#     notas = float(input("Insira mais uma nota"))
#     lista.append(notas)
#     if notas < 7:
#         lista1.append(notas)
#         if notas == -1:
#             lista1.pop(-1)
# if notas == -1:
#     lista.pop(-1)
#
# print(f'A quantidade de notas inseridas foram {len(notas)}')
# #print(' '.join([str(nota) for nota in notas]))
# print(lista1)
# print(f'A soma dos números são {soma}')
# print(f'A média dos valores significa {soma/tamanho}')

#correção do Renzo
notas = []
while True:
    entrada = input ('Digite um número: ')
    if entrada == '-1':
        break
    notas.append(float(entrada))
tamanho =len(notas)
print(f'Foram lidas {tamanho} notas')
print(' '.join([str(nota) for nota in notas]))
#o join une strings, já a list concorrencion é a transformação de cada um dos elementos
# sendo a sintaxte [str (variavel) for variavel in variavel2]
notas.reverse() #reverter a ordem
for nota in notas: #list concorrecion
    print(nota) #looping com for

soma =sum(notas)
print(f'Soma das notas é: {soma}')
media = soma/tamanho
print(f'A média das notas é: {media}')
print(f"Notas acima da média: {', '.join([str(nota) for nota in notas if nota > media ])}") #
print(f"Notas abaixo de sete: {', '.join([str(nota) for nota in notas if nota < 7])}")