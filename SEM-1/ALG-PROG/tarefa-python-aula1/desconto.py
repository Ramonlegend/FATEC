# RA: 1051392411014, 1001392411008
# Nome aluno: Ramon Godinho, Nathan Ferracini
# Data: 26/03/2024
# Descrição: Programa para calcular descontos em compras.

compra1 = float(input("Digite o valor da primeira compra: "))
compra2 = float(input("Digite o valor da segunda compra: "))
compra3 = float(input("Digite o valor da terceira compra: "))

# valor total das compras
valor_total = compra1 + compra2 + compra3

# descontos, acima de 300, acima de 200 e acima de 100 então não usar exemplo: valor_total >= 300.00
if valor_total > 300.00:
  desconto = valor_total * 0.20
elif valor_total > 200.00:
  desconto = valor_total * 0.15
elif valor_total > 100.00:
  desconto = valor_total * 0.10
else:
  desconto = 0.00

valor_final = valor_total - desconto

# valor total e o valor com desconto
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")
print("RA: 1051392411008, Nome: Nathan Ferracini, Turma: 1 semestre DSM ")
print("Valor total das compras: R$", valor_total)
print("Valor com desconto: R$", valor_final)