from random import *

n = randint(0,100)
cont = 0
i = 0

while cont == 0:
    i = i + 1
    resp = int(input('Digite um numero: '))
    if resp == n:
        print('VOCÊ ACERTOU EM %d tentativas' % i)
        cont = cont + 1
    elif resp > n:
        print('TENTE UM NUMERO MENOR')
    else:
        print('TENTE UM NUMERO MAIOR')    