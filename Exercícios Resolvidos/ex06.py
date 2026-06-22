# 6. Contar quantidade de vogais em uma string
texto = input('Digite uma string: ')
quantidade = len([ letra for letra in texto if letra.lower() in 'aeiou'])
print(f'Quantidade de vogais: {quantidade}')