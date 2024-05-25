# def exibirMensagens():
#    print('Olá, tudo bem?')
#    print('Estou no método')


#exibirMensagens()
#print('Até logo!')

# def Spam(x):
#    return x, x, x, x

#print(Spam('spam'))

# def retornavalor(y):
#    return y, 2*y, 3*y, 4*y

#print(retornavalor('João'))


def somaDoisValores(a,b):
    print('Iniciando a soma de valores ...')
    result = a + b
    print('Sua soma foi ralizada com sucesso ...')
    return result

n1 = float(input('Entre com o 1º valor: '))
n2 = float(input('Entre com o 2º valor: '))

print('A soma dos valores é: ', somaDoisValores(n1, n2))