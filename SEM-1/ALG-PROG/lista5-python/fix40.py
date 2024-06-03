# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 13/05/2024
# Descrição: Programa que calcula o aumento de salário de um funcionário de acordo com a regra:
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")


def calcular_aumento(salario):
  if salario <= 1500:
    aumento = salario * 0.2
  elif salario < 2500:
    aumento = salario * 0.1
  elif salario <= 0:
    print("Salário inválido")
  else:
    aumento = salario * 0.05
  novo_salario = salario + aumento
  return novo_salario

nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))

novo_salario = calcular_aumento(salario)

print(f"Olá {nome}, seu novo salário é de R${novo_salario:.2f}")