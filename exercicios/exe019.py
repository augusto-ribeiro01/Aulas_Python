# sotea um nome

import random as rd

nome_1 = input('primeiro aluno: ')
nome_2 = input('segundo aluno: ')
nome_3 = input('terceiro aluno: ')
nome_4 = input('quarto aluno: ')

lista = [nome_1, nome_2, nome_3, nome_4]

sorteio = rd.choice(lista)

print(f" O aluno sortiado foi {sorteio}.")
