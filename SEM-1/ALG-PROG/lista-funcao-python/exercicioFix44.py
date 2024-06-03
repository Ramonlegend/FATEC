# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 23/04/2024
# Descrição: Recebe um valor e executa uma operação de acordo com as condições.
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")

import math

def valor_trabalhado(valor):
    if valor in [1, 2]:
        resultado = valor ** 3
        return f"O valor elevado ao cubo é: {resultado}"
    elif valor % 3 == 0:
        resultado = math.factorial(valor)
        return f"O fatorial do valor é: {resultado}"
    elif valor in [4, 5, 7, 8]:
        resultado = valor / 9
        return f"O valor dividido por 9 é: {resultado}"
    else:
        return "Valor inválido!"

valor = int(input("Digite um valor: "))
print(valor_trabalhado(valor))