# conversão de temperatura

cent = float(input("Informe a temperatura em C°: "))


convercao = cent * 1.8 + 32

print("A tem peratura em C° é {:.3}C° e a convertendo ficara {:.3}F°".format(cent,convercao))