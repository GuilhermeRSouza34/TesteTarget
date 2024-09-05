# 1. Verificar se um número pertence à sequência de Fibonacci
def fibonacci_check(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

# Entrada para o número da sequência de Fibonacci
num = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

if fibonacci_check(num):
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")
