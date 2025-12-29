#O dobro o triplo e a raiz quadrada

number = int(input("Digite um número: "))

print("vamos amostra para você o dobro, o triplo e a raiz quadrada!")

ddobro = number * 2
triplo = number * 3
raiz = number ** (1/2)

print ("o dobro de {} é {} o triplo é {} e essa é a raiz quadrada {:.3} !".format(number,ddobro,triplo,raiz))
