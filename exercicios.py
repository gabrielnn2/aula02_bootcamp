# Inteiros (int)
## 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# numero1 = int(input("Digite o primeiro número: "))
# numero2 = int(input("Digite o segundo número: "))
# soma = numero1 + numero2
# print(f"{numero1} + {numero2} = {soma}")

## 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# divisor = 5
# numero = int(input("Difite o número: "))
# resto = numero % divisor
# print(f"O resto de {numero} dividido por {divisor} é {resto}")

## 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# numero1 = int(input("Digite o primeiro número: "))
# numero2 = int(input("Digite o segundo número: "))
# multiplicacao = numero1 * numero2
# print(f"{numero1} * {numero2} = {multiplicacao}")

## 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# numero1 = int(input("Digite o primeiro número: "))
# numero2 = int(input("Digite o segundo número: "))
# divisao_inteira = numero1 // numero2
# print(f"{numero1} // {numero2} = {divisao_inteira}")

## 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# numero = int(input("Digite o número: "))
# quadrado = numero**2
# print(f"{numero} ao quadrado é {quadrado}")

#Números de Ponto Flutuante (float)

## 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

# numero1 = float(input("Digite o primeiro número: "))
# numero2 = float(input("Digite o segundo número: "))
# soma = numero1 + numero2
# print(f"{numero1} + {numero2} = {soma}")

## 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# numero1 = float(input("Digite o primeiro número: "))
# numero2 = float(input("Digite o segundo número: "))
# media = (numero1 + numero2) / 2
# print(f"A média de {numero1} e {numero2} é {media}")

## 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# base = int(input("Digite a base: "))
# expoente = int(input("Digite o expoente: "))
# potencia = base**expoente
# print(f"{base} elevado a {expoente} é {potencia}")

## 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# temperaturaCelsius = float(input("Insira a temperatura em graus Celsius: "))
# temperaturaFarenheit = (temperaturaCelsius * 9 / 5) + 32
# print(f"{temperaturaCelsius}ºC é equivalente a {temperaturaFarenheit}ºF")

## 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# import math
# raio = float(input("Qual o raio do círculo? "))
# area = math.pi * raio**2
# print(f"A área do círculo de raio {raio} é {area:.2f}")

# Strings (str)

## 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# palavra = input("Digite a string: ")
# palavra_maiuscula = palavra.upper()
# print(palavra_maiuscula)

## 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# nome = input("Digite seu nome completo: ")
# nome_maiusculas = nome.upper()
# print(nome_maiusculas)

## 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# frase = input("Digite uma frase: ")
# frase_tratada = frase.strip()
# print(frase_tratada)

## 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# data = input("Digite uma dara no formato dd/mm/aaaa: ")
# data_tratada = data.split("/")
# print(f"dia: {data_tratada[0]}")
# print(f"mês: {data_tratada[1]}")
# print(f"ano: {data_tratada[2]}")

## 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# string1 = input("Digite a primeira string: ")
# string2 = input("Digite a segunda string: ")
# concatena = string1 + string2
# print(concatena)

# Booleanos (bool)

## 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# boolean1 = input("Digite o primeiro boolean: ")
# boolean2 = input("Digite o segundo boolean: ")
# boolean1 = boolean1 == "True"
# boolean2 = boolean2 == "True"

# resultado = boolean1 and boolean2
# print(resultado)

## 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# boolean1 = input("Digite o primeiro boolean: ")
# boolean2 = input("Digite o segundo boolean: ")
# boolean1 = boolean1 == "True"
# boolean2 = boolean2 == "True"
# resultado = boolean1 or boolean2
# print(resultado)

## 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

# boolean = input("Digite o valor booleano: ")
# boolean = boolean == "True"
# boolean_tratado = not boolean
# print(boolean_tratado)


## 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

# try:
#     numero1 = float(input("Digite o primeiro número: "))
#     numero2 = float(input("Digite o segundo número: "))
#     comparacao = numero1 == numero2
#     print(comparacao)
# except Exception as e:
#     print(e)

## 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# numero1 = float(input("Digite o primeiro número: "))
# numero2 = float(input("Digite o segundo número: "))
# resultado = numero1 != numero2
# print(resultado)

# Desafios

## 21: Conversor de Temperatura
## Escreva um programa que converta a temperatura de Celsius para Fahrenheit.
## O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except,
## garantir que a entrada seja numérica, tratando qualquer ValueError.
## Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

# try:
#     temperaturaCelsius = float(input("Digite a temperatura em °C: "))
#     temperaturaFarenheit = temperaturaCelsius * 9/5 + 32
#     print(f"{temperaturaCelsius}°C é equivalente a {temperaturaFarenheit}°F")
# except ValueError as e:
#     print(e)

## 22: Verificador de Palíndromo
## Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente
## de trás para frente, desconsiderando espaços e pontuações). Utilize try-except para
## garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.

# import re
# entrada = input("Digite uma frase ou palavra: ")

# if isinstance(entrada, str):
#     entrada_tratada = re.sub(r'[^\w\s]','',entrada.lower().replace(" ",""))
#     eh_palindromo = entrada_tratada == entrada_tratada[::-1]
#     print(eh_palindromo)
# else:
#     print("A variável de entrada não é uma string.")


## 23: Calculadora Simples
## Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador
## (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas.
## Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido.
## Imprima o resultado ou uma mensagem de erro apropriada.

# try:
#     numero1 = float(input("Número 1: "))
#     numero2 = float(input("Número 2: "))
#     operador = input("Escolha o operador (+, -, *, /): ")
#     if (operador == "+"):
#         resultado = numero1 + numero2
#     elif (operador == "-"):
#         resultado = numero1 - numero2
#     elif (operador == "*"):
#         resultado = numero1 * numero2
#     elif (operador == "/"):
#         resultado = numero1 / numero2

#     print(f"{numero1} {operador} {numero2} = {resultado}")

# except Exception as e:
#     print(e)

## 24: Classificador de Números
## Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except
## para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número
## como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".

# try:
#     numero = float(input("Digite um número: "))
#     if numero > 0: print(f"{numero} é positivo")
#     elif numero < 0: print(f"{numero} é negativo")
#     elif numero ==0: print(f"{numero} é igual a zero")
#     if numero % 2 == 0: print(f"e é par")
#     else: print(f"e é ímpar")
# except ValueError as e:
#     print(e)

## 25: Conversão de Tipo com Validação
## Crie um script que solicite ao usuário uma lista de números separados por vírgula.
## O programa deve converter a string de entrada em uma lista de números inteiros.
## Utilize try-except para tratar a conversão de cada número e validar que cada elemento
## da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro,
## imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos,
## imprima a lista de inteiros.

# try:
#     lista = input("Digite uma lista de números separados por vírgula: ")
#     lista = lista.split(",")
#     for i in range(len(lista)):
#         lista[i] = int(float(lista[i]))
#     print(lista)
# except Exception as e:
#     print(e)