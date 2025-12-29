distancia = float(input('Qual é a distância da viagem? '))
print(f'Você esta prestes a começar uma viagem de {distancia}km.\n')

if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45

print(f'O preço da sua passagem ficou de R${preço:.2f} \n')
