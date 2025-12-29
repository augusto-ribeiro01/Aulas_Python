number = int(input("Digite um número de 1 a 10: "))

r = number % 2

if r == 0:
    print(f'O número {number} é par!')
else:
    print(f'O número {number} é impar!')
