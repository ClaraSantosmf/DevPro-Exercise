# maximo = float(input("Digite um número de parâmetro inicial: "))
# for _ in range(4):
#    maximo =max(maximo, float(input("digite outro numero: ")))
#    print(f'Número máximo encontrado até agora é {maximo}')
# print("Fim")
soma = 0
media = 0
for c in range (5):
    nota = float(input("Digite uma das notas"))
    soma += nota
media = soma / (c+1)
print(c)
print(soma, media)