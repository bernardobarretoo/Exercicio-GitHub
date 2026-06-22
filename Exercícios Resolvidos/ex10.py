# 10. Dada uma lista numérica, retorne apenas os números positivos

aleatorios = [22, -1, 0, -33, -450, 23, 1, 5945, -337, 2423, 63, -11, 68, 32, -2]

positivos_e_zero = [numero for numero in aleatorios if numero > 0]  

print(f'Positivos: {positivos_e_zero}')