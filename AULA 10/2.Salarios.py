mes = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

totalsalario = 0

for i in range(12):
    salario = float(input('Digite o salario de %s R$ ' %mes[i]))
    totalsalario = totalsalario + salario
    
decimoTerceiro = totalsalario / 12
terçoFerias = decimoTerceiro * (1/3)

print(f'''O salario anual é de R$ {totalsalario}
      O valor do decimo terceiro sera de R$ {decimoTerceiro}
      O valor de 1 / 3 das ferias é de R$ {terçoFerias}''')