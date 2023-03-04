"""
Faça um jogo para o usuário advinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

palavra_secreta = 'abacaxi'
letras_acertadas = ''
tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    tamanho_letra_invalida = len(letra_digitada) > 1
    palavra_formada = ''
    tentativas += 1

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    if tamanho_letra_invalida is not True:
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*'
        print(f'Palavra formada: {palavra_formada}')
    else:
        print('Digite apenas "1" letra por vez.')
        continue
    
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Parabéns, você acertou a palavra secreta!')
        print(f'A palavra secreta era: "{palavra_secreta}"')
        print(f'Tentativas utilizadas: "{tentativas}x"')
        letras_acertadas = ''
        tentativas = 0

