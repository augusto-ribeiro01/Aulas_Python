# aumento de salario

salario = float(input('Qual é o seu salário do funcionário? R$'))

if salario <= 1250:
    novo_s = salario + (salario * 15 / 100)
else:
    novo_s = salario + (salario * 10 / 100)

print(f'Quem ganhava R${salario:.2f} passa a ganhar R${novo_s:.2f}')


