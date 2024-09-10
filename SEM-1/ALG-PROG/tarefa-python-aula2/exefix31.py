# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 06/04/2024
# Descrição: Recebe um valor e realiza uma operação de acordo com o valor digitado.
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")

valor = int(input("Digite um valor: "))

if valor in [1, 2, 3]:
  resultado = valor ** 2
  print(f"O valor elevado ao quadrado é: {resultado}")
elif valor in [4, 9]:
  resultado = valor ** 0.5
  print(f"A raiz quadrada do valor é: {resultado:.0f}")
elif valor in [6, 7, 8]:
  resultado = valor / 9
  print(f"O valor dividido por 9 é: {resultado}")
else:
  print("Valor inválido.")