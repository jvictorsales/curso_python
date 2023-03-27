# Manipulando chaves e valores em dicionários

# pessoa = {
#     'nome': 'João Victor',
#     'sobrenome': 'Sales',
#     'idade': 18,
#     'altura': 1.9,
#     'enderecos': [
#         {'rua': 'tal tal', 'numero': 123},
#         {'rua': 'outra rua', 'numero':321},
#     ],
# }

pessoa = {}

chave = 'nome'

pessoa[chave] = 'João Sales'
pessoa['sobrenome'] = 'Miranda'

print(pessoa)
print(pessoa[chave])

pessoa[chave] = 'Maria'
del pessoa['sobrenome']

print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome', None))

if pessoa.get('sobrenome') is None:
    print('Não existe!')
else:
    print(pessoa['sobrenome'])
