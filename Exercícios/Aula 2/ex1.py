#Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição, subtração, multiplicação, divisão e 
#potenciação do primeiro elevado ao segundo número.

num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))

adição = print(f"\nAdição: {round(num1 + num2, 1)}")
subtração = print(f"Subtração: {round(num1 - num2, 1)}")
multiplicação = print(f"Multiplicação: {round(num1 * num2, 1)}")
divisão = print(f"Divisão: {round(num1 / num2, 1)}")
potenciação = print(f"Potenciação: {round(num1**num2, 1)}\n")