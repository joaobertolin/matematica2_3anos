print("Primeira Competição de Programação da Start")
etapa = "Segunda"
print(etapa, "Competição de Programação da Start")
print(f"{etapa} Competição de Programação da Start")

ficcao = 12
nao_ficcao = 7
infantil = 5

total_pontos = ficcao + nao_ficcao + infantil
print(f"Rodrigo acumulou {total_pontos} pontos.")

fig_total = int(input("Informe o total de figurinhas: "))
amigos = int(input("Informe a quantidade de amigos: "))
fig_por_amigo = fig_total // (amigos + 3)
fig_joao = 2 * fig_por_amigo
print(f"João ficou com {fig_joao} figurinhas.")

alunos = int(input("Informe número de alunos: "))
monitores = int(input("Informe número de monitores: "))
permitido = "Entrada Liberada"
negado = "Entrada Negada"
if alunos + monitores <= 50:
    print(permitido)
else:
    print(negado)

porta1 = int(input("Informe posição da porta (0 ou 1): "))
porta2 = int(input("Informe posição da outra porta (0 ou 1): "))
if porta1 == 0 or porta2 == 0:
    print("C")
elif porta1 == 1 and porta2 == 1:
    print("A")
else:
    print("B")

def calcular_filho_mais_velho(idade_mae, idade_filho_a, idade_filho_b):
    idade_filho_c = idade_mae - idade_filho_a - idade_filho_b
    maior_idade = max(idade_filho_a, idade_filho_b, idade_filho_c)
    return idade_filho_c, maior_idade
calcular_filho_mais_velho(68, 12, 30)

def livro_com_mais_paginas(pag1, pag2, pag3, pag4, pag5):
    return max(pag1, pag2, pag3, pag4, pag5)

max_paginas = livro_com_mais_paginas(100, 250, 150, 320, 400)
print(f"O maior número de páginas entre os livros é {max_paginas}.")
