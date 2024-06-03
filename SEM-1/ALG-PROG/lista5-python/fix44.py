# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 13/05/2024
# Descrição: Programa que calcula a média de aproveitamento de um aluno
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")

def calcular_media_aproveitamento(nome, nota1, nota2):
  media = (nota1 + nota2) / 2

  if media >= 9.0:
    conceito = 'A'
  elif media >= 7.0:
    conceito = 'B'
  elif media >= 5.0:
    conceito = 'C'
  elif media >= 3.0:
    conceito = 'D'
  else:
    conceito = 'E'

  return nome, media, conceito

nome_aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

nome, media, conceito = calcular_media_aproveitamento(nome_aluno, nota1, nota2)

print("Nome do aluno:", nome)
print("Média de aproveitamento:", media)
print("Conceito obtido:", conceito)