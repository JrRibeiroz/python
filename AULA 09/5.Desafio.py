def valorIMC(peso,altura):
    return peso / (altura ** 2)
    
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

print('Seu calculo IMC é igual a ', valorIMC(peso,altura))