"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código nao tem fim
"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=}, {coluna=}')
        coluna += 1
    linha += 1

print('Acabou')


# while linha <= qtd_linhas:
#     coluna_a = 1
#     while coluna_a <= qtd_colunas:
#         coluna_b = 1
#         while coluna_b <= qtd_colunas:
#             print(f'{linha=}, {coluna_a=}, {coluna_b=}')
#             coluna_b += 1
#         coluna_a += 1
#     linha += 1

# print('Acabou')