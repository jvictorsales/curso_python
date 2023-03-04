"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#........+01234
#........-54321
string = 'ABCDE'  # 5 caracteres (len)
#.........0....1......2...........3....4
#........-5...-4.....-3..........-2...-1
lista = [123, True, 'Joao Sales', 1.2, []]
# print(bool(lista))  # falsy
# print(lista, type(lista))
# print(lista[2].upper(), type(lista[2]))
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))
