"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# texto = iter('Joao')  # __iter__()
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))

# for letra in texto_2
texto_2 = 'Sales'  # iterável
iterador = iter(texto_2)  # iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

print('-' * 20)

for letra in texto_2:
    print(letra)
