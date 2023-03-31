# Função lambda em Python
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.

# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort()
# # sorted(lista)
# print(lista)
# lista.sort(reverse=True)
# print(lista)

lista = [
    {'nome': 'João', 'sobrenome': 'Sales'},
    {'nome': 'Maria', 'sobrenome': 'Helena'},
    {'nome': 'Daniel', 'sobrenome':'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# def ordena(item):
#     return item['nome']

# lista.sort(key=ordena)

# lista.sort(key=lambda item: item['nome'])

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
