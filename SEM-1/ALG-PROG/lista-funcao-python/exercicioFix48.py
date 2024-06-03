# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 23/04/2024
# Descrição: Receba o nome e o salário de um funcionário e realize o cálculo de aumento salarial. Se o salário for menor ou igual a 1500, o aumento é de 20%. Se o salário for maior que 1500 e menor que 2500, o aumento é de 10%. Se o salário for maior ou igual a 2500, o aumento é de 5%.
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")

def calculate_salary_increase():
    name = input("Digite seu nome: ")
    salary = float(input("Digite seu salário: "))
    if salary <= 1500:
        salary += salary * 0.20
    elif 1500 < salary < 2500:
        salary += salary * 0.10
    else:
        salary += salary * 0.05
    print(f"Olá {name}, seu novo salário é R${salary:.2f}")

calculate_salary_increase()