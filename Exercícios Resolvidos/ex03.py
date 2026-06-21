# 3. Considere listas de listas e números. Cada lista, por sua vez, está formada por listas e números, recursivamente. Defina uma função achatar que retorne uma lista plana com todos os números da lista original. Por exemplo, achatar([1, 2, [4, 2], 5, [2, [1, 2, 3], [[1]]], 8]) deverá retornar [1, 2, 4, 2, 5, 2, 1, 2, 3, 1, 8]. Dê duas versões, uma sem compreensões e outra com compreensões. A versão com compreensões não precisa retornar os elementos na ordem em que aparecem os números de esquerda à direita.

#sem compreensões:
def achatar(lista):
    nova =[]
    for numero in lista:
        if type(numero) == list :
            nova.extend(achatar(numero))
        else :
            nova.append(numero)
    return nova


#com compreensões
def achatando(lista):
    if type(lista) != list:
        return [lista]
    return [
        num
        for item in lista
        for num in achatando(item)
    ]

xy = [12,3, [2, 4], 5, [2, [23, 43, [1]]], 8]




