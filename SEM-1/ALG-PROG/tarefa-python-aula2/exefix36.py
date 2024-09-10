# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 06/04/2024
# Descrição: divisibilidade
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")

def verificar_divisibilidade(numero):
  if numero % 10 == 0 and numero % 5 == 0 and numero % 2 == 0:
    return f"{numero} é divisível por 10 e 5 e 2"
  elif numero % 10 == 0 and numero % 5 == 0 and numero % 2 != 0: 
    return f"{numero} é divisível por 10 e 5"
  elif numero % 10 == 0 and numero % 5 != 0 and numero % 2 == 0:
    return f"{numero} é divisível por 10 e 2"
  elif numero % 10 != 0 and numero % 5 == 0 and numero % 2 == 0:
    return f"{numero} é divisível por 5 e 2"
  elif numero % 10 == 0 and numero % 5 != 0 and numero % 2 != 0:
    return f"{numero} é divisível por 10"
  elif numero % 10 != 0 and numero % 5 != 0 and numero % 2 == 0:
    return f"{numero} é divisível por 2"
  elif numero % 10 != 0 and numero % 5 == 0 and numero % 2 != 0:
    return f"{numero} é divisível por 5"
  else:
    return f"{numero} não é divisível por 10, 5 ou 2"

numero = int(input("Digite um número: "))
resultado = verificar_divisibilidade(numero)
print(resultado)