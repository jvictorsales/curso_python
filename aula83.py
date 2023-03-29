# Exercício - Sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2 ?',
        'Opcoes': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5 ?',
        'Opcoes': ['25', '55', '10', '51'],
        'Resposta':'25',
    },
    {
        'Pergunta': 'Quanto é 10/2 ?',
        'Opcoes': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

# for questao in perguntas:
#     print('Pergunta:', questao.get('Pergunta'))
#     print()
#
#     print('Opções:')
#     opcoes = questao.get('Opcoes')
#     for indice, opcao in enumerate(opcoes):
#         print(f'{indice}) {opcao}')
#    
#     resposta_indice = input('Escolha uma opção: ')
#     
#     try:
#         resposta_indice = int(resposta_indice)
#         resposta_correta = questao.get('Resposta')
#
#         if opcoes[resposta_indice] == resposta_correta:
#             print('Acertou!')
#         else:
#             print('Errou!')
#
#     except ValueError:
#         print('Opção inválida!')
#     except IndexError:
#         print('Esse opção não existe!')
#
#     print()

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()
    
    opcoes = pergunta['Opcoes']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    
    print()

    escolha = input('Escolha uma opção: ')
    
    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)
    
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')    
    
    print()

print('Você acertou', qtd_acertos, 'de', len(perguntas), 'perguntas.')
