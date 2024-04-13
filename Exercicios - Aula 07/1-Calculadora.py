op = input('Qual operação deseja realizar? (+, -, *, /)')

if op == '+':
    n1 = float(input('Numero a ser somado: '))
    n2 = float(input('+ o Numero: '))
    res = n1 + n2
    print('A soma dos numeros é igual a: ', res)
elif op == '-':
    n1 = float(input('Numero a ser subtraido: '))
    n2 = float(input('- o Numero: '))
    res = n1 - n2
    print('A soma dos numeros é igual a: ', res)
elif op == '*':
    n1 = float(input('Numero a ser multiplicado: '))
    n2 = float(input('x o Numero: '))
    res = n1 * n2
    print('A soma dos numeros é igual a: ', res)
elif op == '/':
    n1 = float(input('Numero a ser dividido: '))
    n2 = float(input('/ pelo Numero: '))
    res = n1 / n2
    print('A soma dos numeros é igual a: ', res)
else:
    print('Opção invalida.')