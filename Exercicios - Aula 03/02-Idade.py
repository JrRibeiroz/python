ano = int(input('Quantos anos você tem? '))
mes = int(input(f'{ano} ano(s) e quantos meses? '))
dia = int(input(f'{ano} ano(s), {mes} mês(es) e quantos dias? '))

dias = (ano*365)+(mes*30)+dia

print(f'Você possui {dias} dias de vida 😄')