def somaDoisValores(a,b):
    result = a + b
    return result

def subDoisValores(a,b):
    result = a - b
    return result

def multDoisValores(a,b):
    result = a * b
    return result

def divDoisValores(a,b):
    result = a / b
    return result

ope = input('''Qual operação deseja realizar?
      1. Soma (+)
      2. Subtração (-)
      3. Multiplicação (+)
      4. Divisão (/)
      ''')

n1 = float(input('Entre com o 1º valor: '))
n2 = float(input('Entre com o 2º valor: '))


if ope == '1' or ope == "+":
    print('Iniciando a soma de valores ...')
    print('Sua soma foi ralizada com sucesso ...')
    print('A soma dos valores é: ', somaDoisValores(n1, n2))
    
elif ope == '2' or ope == '-':
    print('Iniciando a subtração de valores ...')
    print('Sua subtração foi ralizada com sucesso ...')
    print('A subtração dos valores é: ', subDoisValores(n1, n2))

elif ope == '3' or ope =='*':
    print('Iniciando a multiplicação de valores ...')
    print('Sua multiplicação foi ralizada com sucesso ...')
    print('A multiplicação dos valores é: ', multDoisValores(n1, n2))
    
elif ope == '4' or ope == '/':
    print('Iniciando a divisão de valores ...')
    print('Sua divisão foi ralizada com sucesso ...')
    print('A divisão dos valores é: ', divDoisValores(n1, n2))

else:
    print('Operação invalida')