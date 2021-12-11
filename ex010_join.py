#criação de lista se dar pelo = e [], podendo os append inserir elementos na lista
lista = [] #sintaxe da lista
for _ in range (3): # utilizando uma variável genérica com _, e o range cinco vezes.
    numero = float(input('Digite um número para inserir na lista: '))
    lista.append(numero)
lista1 = sorted(lista)
lista1.reverse()
print(lista1)