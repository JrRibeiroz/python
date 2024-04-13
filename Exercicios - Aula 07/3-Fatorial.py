n = int(input('Digite um numero: '))
soma = 1

for i in range(n, 0, -1):
    soma *= i

print(f'O numero {n}! (fatorial) é igual a {soma}')