# Aula 1
# Código 1
print("I Competição de Programação da Start")

# Código 2
ano = "II"
print(ano, "Competição de Programação da Start")

# Código 3
print(f"{ano} Competição de Programação da Start")

# Aula 2
# Código 1
livro_ficcao = 10
livro_nficcao = 8
livro_infantil = 6

pontos_rodrigo = livro_ficcao + livro_nficcao + livro_infantil

print(f"Os pontos totais do Rodrigo são: {pontos_rodrigo}")

# Aula 3
# Código 1
total_figurinhas = int(input("Digite o total de figurinhas: "))
numero_amigos = int(input("Digite o número de amigos: "))

figurinhas_amigos = total_figurinhas // (numero_amigos + 2)
figurinhas_joao = 2 * figurinhas_amigos

print(f"João recebeu {figurinhas_joao} figurinhas.")

# Aula 4
# Código 1
numero_alunos = int(input("Digite a quantidade de alunos: "))
numero_monitores = int(input("Digite a quantidade de monitores: "))

resposta_positiva = "Pode ir"
resposta_negativa = "Não pode ir"

if numero_alunos + numero_monitores <= 50:
    print(resposta_positiva)
else:
    print(resposta_negativa)

# Aula 5
# Código 1
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

# Aula 6
# Código 1
def calcula_idade_maior(idade_monica, idade_filho1, idade_filho2):
    idade_filho3 = idade_monica - idade_filho1 - idade_filho2

    idade_maxima = max(idade_filho1, idade_filho2, idade_filho3)

    return idade_filho3, idade_maxima

calcula_idade_maior(68, 12, 30)

# Aula 7 (Desafio)
# Código 1
# Função para descobrir o maior número de páginas entre 5 livros
def livro_mais_longo(p1, p2, p3, p4, p5):
    return max(p1, p2, p3, p4, p5)

# Exemplo de uso
maior_livro = livro_mais_longo(100, 250, 150, 320, 400)
print(f"O livro com mais páginas tem {maior_livro} páginas.")
