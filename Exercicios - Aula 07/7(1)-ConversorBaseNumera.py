n = int(input('Digite um numero decimal: '))
base = int(input('''Escolha a base de conversão: 
             1 - Binario
             2 - Octal
             3 - Hexadecimal
             
             Digite o numero da sua opção: '''))

if base == 1:
    resp = bin(n)
elif base == 2:
    resp = oct(n)
elif base == 3:
    resp = hex(n)
else:
    print('Opção invalida')

print(f'O numero {n} em base {base} é: {resp}')