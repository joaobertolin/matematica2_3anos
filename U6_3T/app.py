print("I Competição de Programação da Start")
ano = "II"

print(ano, "Competição de Programação da Start")
print(f"{ano} Competição de Programação da Start")

livro_ficcao = 10
livro_nficcao = 8
livro_infantil = 6

pontos_rodrigo = livro_ficcao + livro_nficcao + livro_infantil
print(f"Os pontos totais do Rodrigo são: {pontos_rodrigo}")

total_figurinhas = int(input("Digite o total de figurinhas: "))
numero_amigos = int(input("Digite o número de amigos: "))
figurinhas_amigos = total_figurinhas // (numero_amigos + 2)
figurinhas_joao = 2 * figurinhas_amigos
print(f"João recebeu {figurinhas_joao} figurinhas.")

numero_alunos = int(input("Digite a quantidade de alunos: "))
numero_monitores = int(input("Digite a quantidade de monitores: "))
resposta_positiva = "Pode ir"
resposta_negativa = "Não pode ir"
if numero_alunos + numero_monitores <= 50:
    print(resposta_positiva)
else:
    print(resposta_negativa)

p = int(input("Digite a posição da porta (0 ou 1):"))
r = int(input("Digite a posição da porta (0 ou 1):"))
if p == 0 and r == 0:
    print("C")
elif p == 0 and r == 1:
    print("C")
elif p == 1 and r == 1:
    print("A")
else:
    print("B")

def calcula_idade_maior(idade_monica, idade_filho1, idade_filho2):
    idade_filho3 = idade_monica - idade_filho1 - idade_filho2
    idade_maxima = max(idade_filho1, idade_filho2, idade_filho3)
    return idade_filho3, idade_maxima
calcula_idade_maior(68, 12, 30)

def livro_mais_longo(p1, p2, p3, p4, p5):
    return max(p1, p2, p3, p4, p5)

# Exemplo de uso
maior_livro = livro_mais_longo(100, 250, 150, 320, 400)
print(f"O livro com mais páginas tem {maior_livro} páginas.")
