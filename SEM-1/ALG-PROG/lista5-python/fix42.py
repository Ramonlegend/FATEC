# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 13/05/2024
# Descrição: programa que calcula a maior nota de uma turma de 5 alunos
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")

notas = []
i = 1
while i <= 5:
  nota = float(input(f"Informe a nota do aluno {i}: "))
  notas.append(nota)
  i += 1

maior_nota = notas[0]
for nota in notas:
  if nota > maior_nota:
    maior_nota = nota

print(f"A maior nota da turma é: {maior_nota}")