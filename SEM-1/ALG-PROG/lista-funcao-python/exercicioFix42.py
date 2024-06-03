# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 23/04/2024
# Descrição: Calcula a média de um aluno e verifica se ele foi aprovado ou não.
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")

def student_grade():
    nome = input("Digite seu nome: ")
    ra = input("Digite seu RA: ")
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))

    media = (nota1 + nota2) / 2

    if media >= 7:
        print(f"Parabéns {nome}, sua média é {media:.2f} Você está aprovado!")
    else:
        print(f"Você ainda tem uma chance, {nome}! Estude mais para o exame")

student_grade()