n = int(input('Digite um numero: '))
soma = 0
for i in range(1,n+1):
    if n % i == 0:
        soma += 1
if soma == 2:
    print(f'O numero {n} é primo!')
else:
    print(f'O numero {n} NÃO é primo!')