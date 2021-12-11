# Faça um programa para imprimir: para um n informado pelo usuário.
# Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

# Explicações: Nesse exercício vamos usar a função
# O parâmetro de DEF pode receber um valor e, após os :, podemos informar qual valor que esperamos para esse parâmetro
# o 1ª for executará a própria linha até n + 1 vezes, indicando em i qual é o número do looping que está
# o 2º for executará o print a quantidade de i que houver, porque esse é parâmetro.
# Nesse caso, i guarda nosso objeto desejado, que é o número, que coincide com o número do looping que estamos
# ao final do print existe um comendo omisso do \n. É possível alterar os caractereses finais ocultos por meio de end=

n = int(input("Insira o número máximo de seu triangulo numérico igual: "))
x = int(input("Insira o número máximo de seu triangulo numérico crescente: "))

def imprimir_triangulo_de_numero(n: int):
    for i in range(1, n + 1):
        for _ in range(i):
            print(i, end='   ')
        print('')

def imprimir_triangulo_de_numero_crescente (x: int):
    for linha in range(1, x + 1):
        for coluna in range(1, linha + 1):
            print(coluna, end='   ')
        print('')

print('Aqui está seu triangulo númerico')
imprimir_triangulo_de_numero(n)

print('Aqui está seu triangulo númerico')
imprimir_triangulo_de_numero_crescente(x)