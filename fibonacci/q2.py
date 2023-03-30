def verifica_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n:
        return True
    else:
        return False


numero = int(input("Digite um número: "))

if verifica_fibonacci(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")
