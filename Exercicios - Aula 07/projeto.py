print('-----INTEGRANTES DO GRUPO------')
print('Nome: José Afoso, RGM: 3830....')
print('Nome: José Afoso, RGM: 3830....')
print('Nome: José Afoso, RGM: 3830....')
print('Nome: José Afoso, RGM: 3830....')
print('Nome: José Afoso, RGM: 3830....')
print('-----INTEGRANTES DO GRUPO------')

print('Seja bem vindo ao nosso sistema de conversão de bases')
print('Por favor, escolha uma opção: ')
print('1 - converter de DECIMAL para BINARIO')
print('2 - converter de DECIMAL para HEXADECIMAL')
print('3 - converter de DECIMAL para OCTAL')
print('4 - converter de BINARIO para DECIMAL')
print('5 - converter de HEXADECIMAL para DECIMAL')
print('6 - converter de OCTAL para DECIMAL')
print('0 - Para encerrar o sistema.')

escolha = int(input('Digite a sua escolha: '))

# DECIMAL PARA BINARIO 
def decimal_para_binario(decimal):
    if decimal == 0:
        return '0'
    binario = ''
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal = decimal // 2
    return binario

# DECIMAL PARA HEXADECIMAL:
def decimal_para_hexadecimal(decimal):
    if decimal == 0:
        return '0'
    hexa = ''
    while decimal > 0:
        resto = decimal % 16
        hexa = str(resto) + hexa
        decima = decima // 16
    return hexa
            

# DECIMAL PARA OCTAL:
def decimal_para_octal(decimal):
    if decimal == 0:
        return '0'
    octal = ''
    while decimal > 0:
        resto = decimal % 8
        octal = str(resto) + octal
        decimal = decimal // 8
    return octal

# BINARIO PARA DECIMAL: 
def binario_para_decimal(binario):
    decimal = 0
    expoente = 0
    for bit in reversed(binario):
        decimal += int(bit) * (2 ** expoente)
        expoente += 1
    return decimal

# OCTAL PARA DECIMAL:
def octal_para_decimal(octal):
    decimal = 0
    pot = 0
    for i in reversed(octal):
        decimal += int(i) * (8 ** pot)
        pot += 1
    return decimal

    

while escolha > 0:
    
    numero = int(input('Digite o numero que deseja converter: '))
    
    if escolha == 1:
        print('-----DECIMAL para BINARIO-----')
        binario = decimal_para_binario(numero)
        print('O valor', numero, 'convertido para binario é: ', binario)
        escolha = 0
    elif escolha == 2:
        print('-----DECIMAL para HEXADECIMAL-----')
        escolha = 0
    elif escolha == 3:
        print('-----DECIMAL para OCTAL-----')
        octal = decimal_para_octal(numero)
        print('O valor', numero, 'convertido para octal é: ', octal)
        escolha = 0
    elif escolha == 4:
        print('-----BINARIO para DECIMAL-----')
        decimal = binario_para_decimal(str(numero))
        print('O valor', numero, 'convertido para decimal é: ', decimal)
        escolha = 0
    elif escolha == 5:
        print('-----HEXADECIMAL para DECIMAL-----')
        escolha = 0
    elif escolha == 6:
        print('-----OCTAL para DECIMAL-----')
        decimal = octal_para_decimal(str(numero))
        print('O valor', numero, 'convertido para decimal é: ', decimal)
        escolha = 0
    else:
        print('-----Opção invalida-----')
        print('Por favor, escolha uma opção VÁLIDA: : ')
        print('1 - converter de DECIMAL para BINARIO')
        print('2 - converter de DECIMAL para HEXADECIMAL')
        print('3 - converter de DECIMAL para OCTAL')
        print('4 - converter de BINARIO para DECIMAL')
        print('5 - converter de HEXADECIMAL para DECIMAL')
        print('6 - converter de OCTAL para DECIMAL')
        print('0 - Para encerrar o sistema.')
        escolha = int(input('Digite a sua escolha: '))