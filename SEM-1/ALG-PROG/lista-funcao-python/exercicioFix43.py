# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 23/04/2024
# Descrição: Calcula a média de um aluno e verifica se ele foi aprovado ou não com o adicional do exame.
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")

def calculate_grade():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    notaExame = float(input("Digite a nota do exame: "))

    # Calcula a média aritmética
    media = (nota1 + nota2) / 2

    # Calcula a média final considerando a nota do exame
    mediaFinal = (media + notaExame) / 2

    # Verifica se o aluno foi aprovado ou não
    if mediaFinal >= 5:
        print("Parabéns, você aproveitou a sua chance! Está aprovado.")
    else:
        print("Estude mais para a próxima. Você não alcançou o mínimo necessário.")

calculate_grade()