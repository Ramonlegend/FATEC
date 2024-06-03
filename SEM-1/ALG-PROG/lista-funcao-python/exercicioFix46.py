# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 23/04/2024
# Descrição: Receba um valor e faça a seguinte verificação:
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")

def valor():
    value = float(input("Digite um valor: "))
    if value < 0:
        return abs(value)
    elif value > 10:
        other_value = float(input("Digite outro valor: "))
        return abs(value - other_value)
    else:
        return value / 5

print(valor())