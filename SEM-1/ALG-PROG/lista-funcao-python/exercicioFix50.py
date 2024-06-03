# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 23/04/2024
# Descrição: Receba um valor e faça a seguinte verificação:
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")

def process_value():
    value = float(input("Digite um valor: "))
    if value < 0:
        print(abs(value))
    elif value > 10:
        other_value = float(input("Digite outro valor: "))
        print(abs(value - other_value))
    else:
        print(value / 5)

process_value()
# O EXERCÍCIO É IDENTICO AO EXERCÍCIO 46, A ÚNICA DIFERENÇA É QUE O RESULTADO É IMPRESSO NA TELA AO INVÉS DE RETORNADO.