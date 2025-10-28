CONSTANTE_BONUS = 1000

# 1. Solicita ao usuário que digite seu nome

nome = input("Digite seu nome: ")
if any(char.isdigit() for char in nome):
    print("Insira um nome válido")
    exit()
elif len(nome.replace(' ','')) == 0:
    print("Nome em branco")
    exit()

# 2. Solicita ao usuário que digite o valor do seu salário
try:
    salario = float(input("Digite seu salário: "))
    if salario <= 0:
        print("Digite um salário maior que zero")
        exit()
except ValueError:
    print("Digite um número válido")
    exit()

# 3. Solicita ao usuário que digite o valor do bônus recebido
try:
    bonus = float(input("Digite o bônus: "))
    if bonus <= 1:
        print("Digite um bônus maior que 1")
        exit()
except ValueError:
    print("Digite um número válido")
    exit()

# 4. Calcule o bônus final
kpi = CONSTANTE_BONUS + salario * bonus
print(f"Sua KPI é {kpi:.2f}")
