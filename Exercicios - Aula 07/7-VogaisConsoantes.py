frase = input('Digite uma frase: ')
vogal = 0
cons = 0

for i in frase:
    if i.isalpha():
        if i.lower() in 'aeiou':
            vogal += 1
        else:
            cons += 1

print(f'A frase tem {vogal} vogais')
print(f'A frase tem {cons} consoantes')