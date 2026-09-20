print('Retas de triangulos\n')

r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))


if r1 + r2 >r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('O valor informado forma um tringulo')

else:
    print('O valor informado não forma um triangulo')

