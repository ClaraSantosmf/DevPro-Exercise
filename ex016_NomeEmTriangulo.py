#Faça o nome estar na vertial em escada, depois em uma escada invertida.

#Tudo que podemos fazer em termo de fatiamento para um string, eu posso fazer para listas. Por isso é possível utilizar notação de colchetes
#nome =input("Digite seu nome para a escada")
nome= "clara"
while nome != "": #enquanto a variável nome não for um vazia, então o while continuará
    print(nome) #seria o mesmo de dizer print(nome[:])
    nome = nome[ :-1] #redistribuiu para nome, ele mesmo sem o último íncide.

for i in range(len(nome)+1):
  print(nome[:i])


for s in range(len(nome)+1):
    print(nome[:-1])
    nome = nome [:-1]

