# 1) Verificar se um número pertence à sequência de Fibonacci


def pertence_fibonacci(num):
    fib_1, fib_2 = 0, 1
    while fib_1 <= num:
        if fib_1 == num:
            return f"O número {num} pertence à sequência de Fibonacci."
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return f"O número {num} NÃO pertence à sequência de Fibonacci."


num = int(input("Informe um número: "))
print(pertence_fibonacci(num))


# 2) Verificar a existência da letra 'a' em uma string e contar quantas vezes ela aparece


def conta_letra_a(string):
    contador = 0
    for char in string:
        if char.lower() == 'a':
            contador += 1
    return contador


string = input("Digite uma string: ")
quantidade = conta_letra_a(string)
if quantidade > 0:
    print(f"A letra 'a' aparece {quantidade} vezes.")
else:
    print("A letra 'a' não aparece na string.")


# 3) Cálculo do valor da variável SOMA


indice = 12
soma = 0
k = 1

while K < indice:
    K = K + 1
    soma = soma + K

print(soma)  # Saída: 77


# 4) Completar a sequência lógica
# a) 1, 3, 5, 7, ___
#a) Próximo número: 9

# b) 2, 4, 8, 16, 32, 64, ____
#b) Próximo número: 128

# c) 0, 1, 4, 9, 16, 25, 36, ____
#c) Próximo número: 49


