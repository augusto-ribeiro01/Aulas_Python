import random
from time import sleep
print('Adivinhe o número! \n')
print('-=-' * 20)
print('Penso em números de 0 á 5 e você tenta adivinhar!')
print('-=-' * 20)


pc = random.randint(0, 5) # O computador pensa "entre 0 e 5"
player = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(5)
'''Verifica se jogador acertou o número se não verifica se esta na 
lista senão verifica se é diferente'''

if player == pc:
    print(f'Parabéns, você acertou! O número é {pc}!')
elif player > 5 or player < 0:
    print('O seu número não esta nessa lista')
    print('Tente novamente!')
elif player != pc:
    print('Que pena você errou!')
    print(f'O número escolhido foi {pc}!')
    print('Tente novamente!')
else:
    print('Jogue novamente!')