print('Bem vindo ao numero maior\n')

Numero_1 = int(input('Digite o primeiro numero: '))
Numero_2 = int(input('Digite o segundo numero: '))
Numero_3 = int(input('Digite o terceiro numero: '))

if Numero_1 > Numero_2 and Numero_1 > Numero_3:
    print(f'O numero é maior: {Numero_1}')

elif Numero_2 > Numero_1 and Numero_2 > Numero_3:
    print(f'O numero é maior: {Numero_2}')

else:
  print(f'O numero é maior: {Numero_3}')