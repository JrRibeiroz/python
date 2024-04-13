soma = 0

quantos = int(input('Quantos caracteres tem seu numero binario? (max 5): '))

if quantos == 1:
    print('Seu numero binario continua o mesmo.')
elif quantos == 2:
    for i in range(2):
        n = int(input('Digite um numero binario separadamente de tras para frente: '))
        dec = n * (2**i)
        soma = soma + dec
    print(f'O valor decimal do numero digitado é {soma}.')
elif quantos == 3:
    for i in range(3):
        n = int(input('Digite um numero binario separadamente de tras para frente: '))
        dec = n * (2**i)
        soma = soma + dec
    print(f'O valor decimal do numero digitado é {soma}.')

elif quantos == 4:
    for i in range(4):
        n = int(input('Digite um numero binario separadamente de tras para frente: '))
        dec = n * (2**i)
        soma = soma + dec
    print(f'O valor decimal do numero digitado é {soma}.')
elif quantos == 5:
    for i in range(5):
        n = int(input('Digite um numero binario separadamente de tras para frente: '))
        dec = n * (2**i)
        soma = soma + dec
    print(f'O valor decimal do numero digitado é {soma}.')
else:
    print('Alternativa invalida')