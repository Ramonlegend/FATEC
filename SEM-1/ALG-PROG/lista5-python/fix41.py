# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 13/05/2024
# Descrição: Programa que calcula o fatorial de um número inteiro positivo
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")

def calcular_fatorial(numero):
  if numero < 0:
    print("O número deve ser um inteiro positivo.")
    return
  elif numero == 0:
    return 1
  else:
    fatorial = 1
    for i in range(1, numero + 1):
      fatorial *= i
    return fatorial

numero = int(input("Digite um número inteiro positivo: "))
resultado = calcular_fatorial(numero)
print("O fatorial de", numero, "é", resultado)