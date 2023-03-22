"""
Higher Order Functions
Funções de primeira classe
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

print(
    executa(saudacao, 'Bom dia', 'João')
)

print(
    executa(saudacao, 'Bom dia', 'Maria')
)
