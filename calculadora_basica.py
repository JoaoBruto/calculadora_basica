import math
def calculadora():
    print("Bem vindo a calculadora básica.")

num1 = float(input("Digite o primeiro número desejado. "))
num2 = float(input("Digite o segundo número desejado. "))
operacao = input("Digite a operação desejada (+ , - , * , /, **, sqrt ). ")

if operacao == "+":
    resultado = num1 + num2
    print(f"O resultado de {num1} somado com {num2} é {resultado} : ")

elif operacao == "-":
    resultado = num1 - num2
    print(f"O resultado de {num1} subtraido por {num2} é {resultado} : ")

elif operacao == "*":
    resultado = num1 * num2
    print(f"O resultado de {num1} multiplicado por {num2} é {resultado} : ")

elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado de {num1} dividido por {num2} é {resultado} : ")
    else:
        print("Não pode ser feita divisão por zero (0).")

elif operacao == "**":
    resultado = num1 ** num2
    print(f"O resultado de {num1} elevado a {num2} é {resultado} : ")

elif operacao == "sqrt":
        resultado = math.sqrt(num1)
        print(f"A raiz quadrada de {num1} é {resultado}.")

else:
    print("A operação não pode ser concluída. Tente novamente.")