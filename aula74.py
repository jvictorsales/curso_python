# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

conta_1 = multiplica(2, 3, 4)
print(conta_1)


# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(numero):
    if numero % 2 == 0:
        return f'{numero} Par'
    return f'{numero} Ímpar'

print(par_impar(10))
print(par_impar(11))
print(par_impar(12))
print(par_impar(13))
print(par_impar(14))
