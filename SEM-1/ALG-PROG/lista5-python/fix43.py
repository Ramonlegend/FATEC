# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 13/05/2024
# Descrição: Programa que calcula o IMC de uma pessoa e verifica se ela está no peso ideal
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")


peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))
sexo = input("Digite o sexo (M para masculino ou F para feminino): ")

# Calcular o IMC
imc = peso / (altura ** 2)

# Verificar se a pessoa está no peso ideal
if sexo == "M" or sexo == "m" or sexo == "Masculino" or sexo == "masculino":
  peso_ideal_min = 20 * (altura ** 2)
  peso_ideal_max = 25 * (altura ** 2)
else:
  peso_ideal_min = 19 * (altura ** 2)
  peso_ideal_max = 24 * (altura ** 2)

# Exibir o resultado
print("IMC: {:.2f}".format(imc))
if peso >= peso_ideal_min and peso <= peso_ideal_max:
  print("Peso ideal!")
else:
  print("Não está no peso ideal!")