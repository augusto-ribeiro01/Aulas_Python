import random

print('Adivinhe o número! ')
number = int(input('Digite um numero: '))


if random.randint(1,5) == number :
    print(f'Parabens você acertou!')
else:
    print('Que pena você errou!')

