# calculando a hipotenusa

'''import math as mt

cateto_a = float(input("Digite o valor do cateto A: "))
cateto_b = float(input("Digite o valor do cateto B: "))

hipotenusa = mt.hypot(cateto_a, cateto_b)

print(f"Os catetos são {cateto_a} e o {cateto_b}.")
print(f"A sua hipotenusa é {hipotenusa:.2f}")'''


'''from math import hypot as ht

cateto_a = float(input("Digite o valor do cateto A: "))
cateto_b = float(input("Digite o valor do cateto B: "))

hipotenusa = ht(cateto_a, cateto_b)

print(f"Os catetos são {cateto_a} e o {cateto_b}.")
print(f"A sua hipotenusa é {hipotenusa:.2f}")'''

co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adijacrnte: "))

hi = (co ** 2 + ca ** 2) ** (1/2)

print(f"Os catetos são {co} e o {ca}.")
print(f"A sua hipotenusa é {hi:.2f}")

