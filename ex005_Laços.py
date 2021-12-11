# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
# e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A
# ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

A = 80000
B = 200000
taxa_A = 1.03
taxa_B = 1.015
ano = 0

while True:
    if A == B:
        print(f"Demorou {ano} para as populações se igualarem, estando país A com {A} e país B com {B}")
        break
    elif A > B:
        print (f'Demorou {ano} anos para a população de A, com {A} habitantes, ultrapassar a população de B com {B} habitantes')
        break
    elif A != B:
        A *= taxa_A
        B *= taxa_B
        ano += 1
    print(f'{int(A)}')
