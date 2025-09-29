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
