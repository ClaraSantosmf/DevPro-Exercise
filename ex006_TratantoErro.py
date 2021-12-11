#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
# seja inválido e continue pedindo até que o usuário informe um valor válido.
while True:
    try:
        numero = int(input("Forneça um número inteiro entre 0 e 10 "))
    except ValueError:
        print("Erro: O valor deve ser um número inteiro")
    else:
        if 0 <= numero <= 10:
            print(f"O número informado é {numero}")
            break
        else:
           print("O numero deve estar entre 0 e 10")
