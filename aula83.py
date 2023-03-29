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

for questao in perguntas:
    print('Pergunta:', questao.get('Pergunta'))
    print()
    opcoes = questao.get('Opcoes')
    print('Opções:')
    for indice, opcao in enumerate(opcoes):
        print(f'{indice}) {opcao}')
    resposta_indice = input('Escolha uma opção: ')
    try:
        resposta_indice = int(resposta_indice)
        resposta_correta = questao.get('Resposta')
        if opcoes[resposta_indice] == resposta_correta:
            print('Acertou!')
        else:
            print('Errou!')
    except ValueError:
        print('Opção inválida!')
    print()
