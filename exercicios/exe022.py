# faça um código que leia um nome completo de uma pessoa, e apareça o nome com todas as letras maiusculas,
# o nome com todas as letras minusculas, quantas letras aotodo sem considerar espaço e quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()


print (f'esse é seu nome em Maiúslo, {nome.upper()}')
print(f'esse é seu nome em minúsculo, {nome.lower()}')
print(f'a quantidade de letras do seu nome sem espaços é de {len(nome)-nome.count(' ')}')
print(f'esse é o tamanho do seu primeiro nome {nome.find(' ')}')