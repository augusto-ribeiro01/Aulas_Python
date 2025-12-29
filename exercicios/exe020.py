'''import random as rd

nome = ["Augusto", "Debora", "Samuel", "Ester", "paloma", "jhon", "pamela"]

#vai sortea uma sequencia

print(f"lista de aulunos \n {nome}")

rd.shuffle(nome)

print(f"lista reordenada \n {nome}")'''

from random import shuffle as sff

nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
nome3 = input("Digite o terceiro nome: ")
nome4 = input("Digite o quarto nome: ")

nomes = [nome1, nome2, nome3, nome4]

print(f"lista origem dos que vam apresentar: \n")
print(nomes)

sff(nomes)

print("Essa é a sequencia de apresentação! \n")
print(nomes)