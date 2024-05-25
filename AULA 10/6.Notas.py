qtd = int(input('Quantas notas gostaria de inserir? '))
soma = 0

for i in range(1,qtd+1):
    nota = float(input(f'Digite sua {i}ª nota: '))
    soma += nota
    
media = soma / qtd

print(f'Sua media é {media}')