# 1. Defina uma função que leia do teclado uma sequência de números inteiros dados em uma única linha. A função deve retornar uma lista contendo os números que estão na linha.

def ler_sequencia_inteiros():
    #solicito os números ao usuário
    entrada = input('Escreva aqui números INTEIROS separados por espaço: ')
    #transformo esses números solicitados inteiros e em uma lista
    lista_inteiros = [int(numero) for numero in entrada.split()]
    #retorno o print dessa lista 
    return print(lista_inteiros)
    
#chamo a função
ler_sequencia_inteiros()