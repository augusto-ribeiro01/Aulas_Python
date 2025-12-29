print('-=-' * 20)
print('Analisando Triângulo'.center(50))
print('-=-' * 20)

reta_1 = float(input('Primeiro seguimento: '))
reta_2 = float(input('Segundo seguimento: '))
reta_3 = float(input('Terceiro seguimento: '))



if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print(f'Os seguimentos {reta_1}, {reta_2} e {reta_3} podem formar um triângulo!')
else:
    print(f'Os seguimentos {reta_1}, {reta_2} e {reta_3} são incapazes de formar um triângulo!')

