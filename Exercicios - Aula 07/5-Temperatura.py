n = int(input('Digite a temperatura: '))
temp = input('Digite C para Celsius ou F para Fahrenheit: ')

if temp.lower() == 'c':
    conv = (n * 9/5) + 32
    print(f'A temperatura em Fahrenheit é de {conv} F')
elif temp.upper() == 'F':
    conv = (n - 32) * 5/9
    print(f'A temperatura em Celsius é de {conv} C')
else:
    print('Opção invalida')