n1 = float(input('Informe o primeiro número da operação: '))
op = input('Qual operação deseja realizar (+ , - , *, /): ')
n2 = float(input('Informe o segundo número da operação: '))

if op == '+':
    input(f'Valor: {n1+n2}')
elif op == '-':
    input(f'Valor: {n1-n2}')
elif op == '*':
    input(f'Valor: {n1*n2}')
elif op == '/':
    input(f'Valor: {n1/n2}')