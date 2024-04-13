n = input('Digite um numero: ')
cont = 0

for i in n:
    if i.isdigit():
        cont += 1
    
print(f'O numero {n} tem {cont} digitos')