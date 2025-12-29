# calculando os metros quadrados para não disperdiça tinta

alt = float(input("Qual a altura da parede?\n"))
larg = float(input("Qual a largura da parede?\n"))

mq = alt * larg
area = mq
tinta_rende = (area * 2) / 10

print("sabemos que um balde de tinta contem 10l \n")
print("Sua parede tem a dimenção de altura {:.2f}x{:.2f} largura e a área é de {:.3f}m² \n".format(alt, larg, area))
print("para pintar essa parede, você gastara {:.3f}l de tinta".format(tinta_rende))