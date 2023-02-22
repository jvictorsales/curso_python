nome = 'Joao Sales'
altura = 1.75
peso = 80
imc = peso / altura ** 2

# f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Joao Sales tem 1.75 de altura,
# pesa 80 quilos e seu IMC é
# 26.12244897959184