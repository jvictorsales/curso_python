"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""

import os

lista_compras = []

while True:
    print('Selecione uma opção')

    opcao = input('[i]nserir [a]pagar [l]istar [s]air: ').lower()

    if opcao.startswith('i'):
        os.system('cls')
        add_item = input('Digite o produto: ')
        lista_compras.append(add_item)
        print(f'Produto "{add_item}" adicionado na lista de compras.')
        print()

    elif opcao.startswith('a'):
        os.system('cls')
        if lista_compras == []:
            print('Lista vazia, não tem o que apagar.')
            continue

        remove_item = input('Digite o índice do produto para apagar: ')

        try:
            remove_item = int(remove_item)

            if remove_item < 0:
                print('Índice inválido, tente novamente.')
                continue

            del (lista_compras[remove_item])
            print(f'Produto "{lista_compras[remove_item]}" removido.')
            print()

        except:
            print('Índice inválido, tente novamente.')

    elif opcao.startswith('l'):
        os.system('cls')
        if lista_compras == []:
            print('Lista vazia, não tem o que exibir.')
            continue

        for indice, produto in enumerate(lista_compras):
            print(indice, produto)

        print()

    elif opcao.startswith('s'):
        os.system('cls')
        print('Encerrando... ')
        print()
        break

    else:
        print('Opção escolhida inválida! Tente novamente.')


# lista_compras = []

# def exibir_lista():
#     for indice, produto in enumerate(lista_compras):
#         print(f'{indice}-', produto)
#     print()

# while True:

#     print(f'\tMENU')
#     print('1- Adicionar um item na lista')
#     print('2- Apagar um item da lista')
#     print('3- Exibir a sua lista')
#     print('4- Sair')

#     opcao = input('Escolha a opção deseja do Menu [1-4]: ')
#     print()

#     try:
#         opcao = int(opcao)

#         if opcao == 1:
#             add_item = input('Adicionar produto: ')
#             lista_compras.append(add_item)
#             print()

#         elif opcao == 2:
#             remover_item = input('Informe o numero do item que deseja remover: ')
#             remover_item = int(remover_item)
#             del(lista_compras[remover_item])
#             print()

#         elif opcao == 3:
#             exibir_lista()

#         elif opcao == 4:
#             print('Saindo ...')
#             print('Segue abaixo a sua lista de compras completa:')
#             exibir_lista()
#             break

#         else:
#             print('Essa opção não existe, tente novamente.')

#     except:
#         print('Opção inválida! Tente novamente.')
