"""
enumerate - enumera iteráveis (índices)
"""

# [(0, 'Maria'), (1, 'Helena'), (2, 'João'), (3, 'Bruna')]
lista = ['Maria', 'Helena', 'João', 'Bruna']
# lista_enumerada = list(enumerate(lista))
# print(lista_enumerada)

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#             print(f'\t{valor}')
