#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros; comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

cobertura_tinta = 6
volume_lata = 18
preco_lata = 80
volume_galao = 3.6
preco_galao = 25
tamanho_area = float(input("Qual é a área que será pintada?"))
import math #biblioteca importada math

litros = tamanho_area/cobertura_tinta
latas_inteiras = (math.ceil(litros/volume_lata)) # latas inteiras minimas necessárias para a área
resto_tinta_lata = litros % volume_lata #quanto falta de tinta.
galoes_inteiro =(math.ceil(litros/volume_galao)) # galões inteiros minimos necessárias para a área?

print(f'O cliente precisará de {latas_inteiras} latas de 18 litros, com custo de R${latas_inteiras * preco_lata}')
print(f'Ou o cliente poderá usar {galoes_inteiro} galões de 3,6 litros, com custo de R${galoes_inteiro * preco_galao}')
print('Visando evitar desperdício, consulte o conselho de compras entre latas e galões:')
galao = (resto_tinta_lata / volume_galao) #galões necessários para completar a falta de tinta deixada pela compra de latas minimas
if litros < volume_lata: #desvio condicional para otimizar a compra entre latas e galões, completando com galões o que faltar com as compras das latas
    print(f'O cliente precisará apenas de uma lata de 18 litros, ou {galoes_inteiro} galões inteiros ao custo de R$ {galoes_inteiro*preco_galao},00')
elif litros > volume_lata:
    print(f'O cliente poderá optar por comprar {math.floor(litros/volume_lata)} lata de tinta, e {math.ceil(galao)} '
          f'galões de tintas com custo de R$ {(math.floor(litros/volume_lata) * preco_lata) + (math.ceil(galao)* preco_galao)},00')
else:
    print(f'O cliente precisará apenas de uma lata de tinta de 18 litros ao custo de R$ 80,00')
