frase = str(input('Digite uma frase: ')).strip().upper()
print(f"A letra A aparece {frase.count('A')} vezes na frase")
print(f"A letra A aparece pela primeira vez na frase {frase.find('A')+1}")
print(f"Em que posição a parece a ultima letra A {frase.rfind('A')+1}")