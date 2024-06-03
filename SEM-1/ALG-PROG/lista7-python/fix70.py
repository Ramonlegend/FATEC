# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 03/06/2024
# Descrição: Programa que calcula a média de um aluno e retorna o conceito de acordo com a média.
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")


class Aluno:
  def __init__(self, nome, nota1, nota2):
    self.nome = nome
    self.nota1 = nota1
    self.nota2 = nota2

  def calcular_media(self):
    return (self.nota1 * 4 + self.nota2 * 6) / 10

  def obter_conceito(self):
    media = self.calcular_media()
    if media >= 9:
      return "A"
    elif media >= 7.5:
      return "B"
    elif media >= 6:
      return "C"
    elif media >= 4:
      return "D"
    else:
      return "E"

nome_aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

aluno = Aluno(nome_aluno, nota1, nota2)
media = aluno.calcular_media()
conceito = aluno.obter_conceito()

print("Nome do aluno:", aluno.nome)
print("Média de aproveitamento:", media)
print("Conceito:", conceito)