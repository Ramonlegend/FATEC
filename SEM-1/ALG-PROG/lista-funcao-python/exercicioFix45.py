# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 23/04/2024
# Descrição: Descubra o valor final de uma compra com desconto de acordo com o valor da compra.
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")

def calculo_desconto():
    valor_compra = float(input("Digite o valor da compra: "))

    if valor_compra > 300:
        desconto = 0.20
    elif 200 <= valor_compra <= 299.99:
        desconto = 0.10
    else:
        desconto = 0.05

    valor_desconto = valor_compra * desconto
    valor_final = valor_compra - valor_desconto

    return f"O valor total da compra é: R$ {valor_compra:.2f}. Com o desconto de {desconto*100}%, o valor final a pagar é: R$ {valor_final:.2f}."

print(calculo_desconto())