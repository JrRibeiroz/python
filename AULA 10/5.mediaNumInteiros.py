notas = []
soma = 0

print('''Digite quantas notas quiser.
      Digite 0 oara sair do sistema''')

while True:
    n = float(input('Digite uma nota: '))
    if (n == 0):
        break

    notas.append(n)
    soma += n
    
media = soma / len(notas)
print('Media %.2f' %media)
print('Notas digitadas')