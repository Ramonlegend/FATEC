# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 13/05/2024
# Descrição: Programa que calcula a média de um aluno
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")

usuario_autenticado = "professor"
senha_autenticada = "senha123"

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_autenticado and senha == senha_autenticada:
    print("Acesso autorizado.\n")

    nome_aluno = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))

    media = (nota1 + nota2) / 2

    if media >= 9.0:
        conceito = "A - APROVADO"
    elif media >= 7.0:
        conceito = "B - APROVADO"
    elif media >= 3.0:
        conceito = "C - EXAME"
    else:
        conceito = "D - DP"

    print(f"\nNome do aluno: {nome_aluno}")
    print(f"Média de aproveitamento: {media:.2f}")
    print(f"Conceito: {conceito}")

else:
    print("Acesso não autorizado. Verifique suas credenciais.")