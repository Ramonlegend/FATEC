# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 03/06/2024
# Descrição: Programa que calcula a média de um aluno e retorna o conceito de acordo com a média.
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")

class calcular_salario:
  def __init__(self, media_hora):
    self.media_hora = media_hora

  def calcular_pagamento(self, hora_trabalhada):
    if hora_trabalhada <= 40:
      salario = hora_trabalhada * self.media_hora
    else:
      hora_extra = hora_trabalhada - 40
      salario = (40 * self.media_hora) + (hora_extra * self.media_hora * 1.5)
    return salario

media_hora = 10.0
hora_trabalhada = float(input("Coloque o numero de horas trabalhadas: "))

calculadora = calcular_salario(media_hora)
pagamento = calculadora.calcular_pagamento(hora_trabalhada)
print("O pagamento é:", pagamento)