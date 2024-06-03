# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 23/04/2024
# Descrição: Recebe um valor e realiza uma operação de acordo com o valor digitado.
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")

import math
def valor_processado(valor):
    if valor in [1, 2, 3]:
        resultado = valor ** 2
        return f"O valor elevado ao quadrado é: {resultado}"
    elif valor in [4, 9]:
        resultado = math.sqrt(valor)
        return f"A raiz quadrada do valor é: {resultado}"
    elif valor in [6, 7, 8]:
        resultado = valor / 9
        return f"O valor dividido por 9 é: {resultado}"
    else:
        return "Valor inválido!"

valor = int(input("Digite um valor: "))
print(valor_processado(valor))