# RA: 1051392411014, 1001392411008
# Nome aluno: Ramon Godinho, Nathan Ferracini
# Data: 26/03/2024
# Descrição: Programa que calcula o peso ideal de uma pessoa.
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")
print("RA: 1051392411008, Nome: Nathan Ferracini, Turma: 1 semestre DSM ")

altura = float(input("Digite a sua altura (exemplo: 1.80): "))
sexo = input("Digite seu sexo (M/F): ")

if sexo.upper() == "M":
  peso_ideal = (72.7 * altura) - 58
elif sexo.upper() == "F":
  peso_ideal = (62.1 * altura) - 44.7
else:
  print("Sexo invalido, digite apenas M ou F!")
  peso_ideal = None

if peso_ideal is not None:
  print("Seu peso ideal é:", peso_ideal, "kg")