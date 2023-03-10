"""
Exercício
Exiba os índices da lista
"""

lista = ['Maria', 'Helena', 'João']
lista.append('Luiz')

# indices = 0
# for nome in lista:
#     print(indices, nome, type(nome))
#     indices += 1

indices = range(len(lista))
for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
