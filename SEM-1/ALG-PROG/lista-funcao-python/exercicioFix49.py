# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 23/04/2024
# Descrição: Receba o nome e a idade de uma pessoa e verifique se ela é menor de idade, maior de idade ou maior de 65 anos.
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")

def check_age():
    name = input("Digite seu nome: ")
    age = int(input("Digite sua idade: "))
    if age < 18:
        print(f"Bem vindo {name}, você é menor de idade.")
    elif 18 <= age < 65:
        print(f"Bem vindo {name}, você é maior de idade.")
    else:
        print(f"Bem vindo {name}, você é maior de 65 anos.")

check_age()