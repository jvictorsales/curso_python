# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}

s1 = set()
print(s1, type(s1))

s1 = set('Luiz')
print(s1, type(s1))

s1 = {'João', 1, 2, 3}
print(s1)

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - eles não tem indexes;
# - eles não garantem ordem;
# - eles são iteráveis (for, in, not in)

print()

l1 = [1, 2, 3, 3, 3, 3, 1]
s2 = set(l1)
l2 = list(s2)
# s2 = {1, 2, 3, 3, 3, 3, 1}
print(s2)
print(l2)

s3 = {1, 2, 3}
print(3 in s3)
print(3 not in s3)
print(4 in s3)

for numero in s3:
    print(numero)

print()

# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add('João')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4))
# s1.clear()
s1.discard('Olá mundo')
s1.discard('João')
print(s1)
print()

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s2 - s1
s3 = s1 ^ s2
print(s3)
