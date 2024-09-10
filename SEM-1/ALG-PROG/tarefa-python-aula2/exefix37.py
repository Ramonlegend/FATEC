# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 06/04/2024
# Descrição: Autorização de aumento salarial
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")

name = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))

if salario <= 1500:
  salario_aumento = salario * 0.2
elif salario > 1500 and salario <= 2500:
  salario_aumento = salario * 0.1
else:
  salario_aumento = salario * 0.05

novo_salario = salario + salario_aumento

print(f'Aumento de {salario_aumento} do seu salário autorizado!')
print(f"Olá, {name}! Seu novo salário é de R${novo_salario:.2f}.")