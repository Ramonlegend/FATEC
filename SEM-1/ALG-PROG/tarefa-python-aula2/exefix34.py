# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 06/04/2024
# Descrição: desconto em compras
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")

valor_compra = float(input("Digite o valor da compra: "))

if valor_compra >= 300:
  desconto = valor_compra * 0.2
elif valor_compra >= 200 and valor_compra <= 299.99:
  desconto = valor_compra * 0.1
else:
  desconto = valor_compra * 0.05

valor_final = valor_compra - desconto

print("Valor total: R$", valor_compra)
print(f"Valor do desconto: R$ {desconto:.2f}")
print("Valor final a pagar: R$", valor_final)