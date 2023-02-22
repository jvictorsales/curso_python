"""
Faça um programa que peça ao usuário para digitar um núnmero inteiro,
informe ser este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero_inteiro = input('Digite um número inteiro: ')

# if numero_inteiro.isdigit():
#     numero_inteiro = int(numero_inteiro)
#     if numero_inteiro % 2 == 0:
#         print('Par')
#     else:
#         print('Ímpar')
# else:
#     print('Você não digitou um número inteiro.')


# numero_inteiro = input('Digite um número inteiro: ')

# try:
#     numero_inteiro = int(numero_inteiro)
#     if numero_inteiro % 2 == 0:
#         print('Par')
#     else:
#         print('Ímpar')    
# except:
#     print('Você não digitou um número inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. 
Ex. Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# hora_informada = input('Digite a hora atual [0-23]: ')

# if hora_informada.isdigit():
#     hora_informada = int(hora_informada)
#     if 0 <= hora_informada <= 11:
#         print('Bom dia!')
#     elif 12 <= hora_informada <= 17:
#         print('Boa tarde!')
#     elif 18 <= hora_informada <= 23:
#         print('Boa noite!')
#     else:
#         print('Você não digitou um valor entre [0-23].')
# else:
#     print('Você não digitou a hora corretamente.')

# hora_informada = input('Digite a hora atual [0-23]: ')

# try:
#     hora_informada = int(hora_informada)
#     if 0 <= hora_informada <= 11:
#         print('Bom dia!')
#     elif 12 <= hora_informada <= 17:
#         print('Boa tarde!')
#     elif 18 <= hora_informada <= 23:
#         print('Boa noite!')
#     else:
#         print('Você não digitou um valor entre [0-23].')
# except:
#     print('Você não digitou a hora corretamente.')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('')
