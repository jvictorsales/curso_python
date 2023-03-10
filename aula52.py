"""
Cuidados com dados mutáveis
= - Copiando o valor (imutáveis)
= - Aponta para o mesmo valor na memória (mutável)
"""

# nome = 'Luiz'
# outra_variavel = nome
# nome = 'João'
# print(nome)
# print(outra_variavel)

lista_a = ['João', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
