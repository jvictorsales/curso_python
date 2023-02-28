# Calculadora com while

while True:

    num_a = input('Digite um número: ')
    num_b = input('Digite outro número: ')
    operador = input('Digite o operador [ + - * / ]: ')
    
    numeros_validos = None
    num_a_float = 0
    num_b_float = 0

    try:
        num_a_float = float(num_a)
        num_b_float = float(num_b)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos or operador == '':
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando a operação ...')
    if operador == '+':
        print(f'{num_a} + {num_b} = {num_a_float + num_b_float}')
    elif operador == '-':
        print(f'{num_a} - {num_b} = {num_a_float - num_b_float}')
    elif operador == '*':
        print(f'{num_a} * {num_b} = {num_a_float * num_b_float}')
    elif operador == '/':
        print(f'{num_a} / {num_b} = {num_a_float / num_b_float}')
    else:
        print('Ocorreu algo inesperado!')
    
    sair = input('Quer sair ? [s]im: ').lower().startswith('s')
    if sair is True:
        break
