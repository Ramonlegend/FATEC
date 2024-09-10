# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 06/04/2024
# Descrição: Realiza a média de duas notas e informa se o aluno foi aprovado ou não.
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")

nome = input("Digite seu nome: ")
ra = input("Digite seu RA: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
  print(f"Parabéns, {nome}! Sua média é {media:.2f}. Você está aprovado!")
else:
  print(f"{nome}, sua média é {media:.2f}. Você ainda tem uma chance! Estude mais para o exame.")

  nota_exame = float(input("Digite a nota do exame: "))

  media_final = (media + nota_exame) / 2

  if media_final >= 5:
    print(f"Parabéns, {nome}! Você aproveitou a sua chance! Está aprovado.")
  else:
    print(f"Estude mais para a próxima, {nome}. Você não alcançou o mínimo necessário.")