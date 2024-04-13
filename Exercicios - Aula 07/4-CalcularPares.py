n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

soma = 0
for i in range(n1, n2+1):
    if i % 2 == 0:
        soma += i

print(f'A soma do intervalo de numeros é {soma}')