"""
Iterando strings com while
"""
#       0123456789
nome = 'João Sales'  # Iteráveis
#     -10987654321

tamanho_nome = len(nome)
nova_string = ''
indice = 0

while indice < tamanho_nome:
    letra = nome[indice]
    nova_string += f'*{letra}'
    indice += 1

    if indice == tamanho_nome:
        nova_string += '*'
        break

print(nova_string)
