# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'João Victor',
#     'sobrenome': 'Sales',
#     'idade': 30,
#     'altura': 1.8,
#     'enderecos': [
#         {'rua': 'tal tal', 'numero': 123},
#         {'rua': 'outra rua', 'numero': 321},
#     ]
# }
# pessoa = dict(nome='João Victor', sobrenome='Sales')
# print(pessoa, type(pessoa))

pessoa = {
    'nome': 'João Victor',
    'sobrenome': 'Sales',
    'idade': 30,
    'altura': 1.8,
    'enderecos': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321},
    ],
}

print(pessoa['nome'])
print(pessoa['sobrenome'])
print()

for chave in pessoa:
    print(chave, pessoa[chave])
