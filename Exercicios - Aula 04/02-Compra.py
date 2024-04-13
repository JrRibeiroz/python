p1 = float(input('Digite o valor do 1º produto: R$ '))
p2 = float(input('Digite o valor do 2º produto: R$ '))
p3 = float(input('Digite o valor do 3º produto: R$ '))
p4 = float(input('Digite o valor do 4º produto: R$ '))
p5 = float(input('Digite o valor do 5º produto: R$ '))

com = p1 + p2 + p3 + p4 + p5
des = com * 20 / 100

if com > 200:
    print('Parabéns! Ganhou desconto de 20% nessa compra.')
    print(f'Valor da compra: R$ {com}')
    print(f'Valor do desconto: R$ {des}')
    print(f'Valor da compra com desconto: R$ {com-des}')

else:
    print(f'Valor da compra: R$ {com}')