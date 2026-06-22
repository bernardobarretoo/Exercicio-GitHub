# 9. Crie uma lista com todos os números primos de 1 a n

n = int(input())

primos_1_to_n = [ numero for numero in range(2, n + 1) if all(numero % i!= 0 for i in range(2, int(numero **0.5) + 1)) ]

print(primos_1_to_n)