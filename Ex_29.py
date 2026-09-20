print('Bem Vindo ao Km certo.')

distancia = float(input('Digite em km a distancia da sua viagem: '))

tarifa_1 = 0.50
tarifa_2 = 0.45

if distancia <= 200:
    preco = distancia * tarifa_1

else:
     preco =  distancia * tarifa_2

print(f'O valor da sua tarifa é R$: {preco:.2f}')

