# seno cosseno e tangente

'''import math as mt

angulo_g = float(input("Digite o angulo do grau:"))

seno = mt.sin(mt.radians(angulo_g))
cosseno = mt.cos(angulo_g)
tangente = mt.tan(angulo_g)

print(f"_____________________ o ângulo do grau é {angulo_g} ____________________\n")
print(f"seno {seno}")
print(f"cosseno {cosseno}")
print(f"tangente {tangente}")'''


from math import radians, sin, cos, tan

angulo_g = float(input("Digite o ângulo do grau:"))

seno = sin(radians(angulo_g))
cosseno = cos(radians(angulo_g))
tangente = tan(radians(angulo_g))

print(f"_____________________ o ângulo do grau é {angulo_g} ____________________\n")
print(f"seno {seno:.2f}")
print(f"cosseno {cosseno:.2f}")
print(f"tangente {tangente:.2f}")



