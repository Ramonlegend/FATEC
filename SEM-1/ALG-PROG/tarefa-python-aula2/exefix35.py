# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 06/04/2024
# Descrição: Realizar operações com números
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")


valor = float(input("Digite um valor: "))

if valor < 0:
  valor_absoluto = abs(valor)
  print("O módulo do valor é:", valor_absoluto)
elif valor > 10:
  novo_valor = float(input("Digite outro valor: "))
  diferenca = valor - novo_valor
  print("A diferença entre os valores é:", diferenca)
else:
  resultado = valor / 5
  print("O valor dividido por 5 é:", resultado)