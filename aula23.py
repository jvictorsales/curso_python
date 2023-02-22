# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 6 7 8 9 10
#  P r o g r a m a d o r
# -11-10-9-8-7-6-5-4-3-2-1

# nome = 'Programador'
# print(nome[2])
# print(nome[-9])

# print('m' in nome)
# print('z' in nome)
# print('gra' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}.')
else:
    print(f'{encontrar} não está em {nome}.')
