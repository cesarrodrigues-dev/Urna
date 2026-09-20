print('Bem vindo ao programa empréstimo pessoal\n')

emprestimo = float(input('Digite o valor do empréstimo: '))

salario = float(input('Digite o valor do salário do comprador: '))

anos = int(input('Em quantos anos deseja pagar?: '))

meses = anos * 12

prestacao = emprestimo / meses

prestacao_br = f'{prestacao:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

if prestacao > salario * 0.3:

    print('Empréstimo negado.')
    print(f'O valor da sua prestação é R$ {prestacao_br}')

else:

    print('Empréstimo aprovado.')
    print(f'O valor da sua prestação é R$ {prestacao_br}')
