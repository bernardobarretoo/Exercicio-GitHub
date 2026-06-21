# 2. Defina a função descendentes que pega uma árvore genealógica e retorna todos os descendentes da raiz. Utilize compreensões.

def descendentes(arv):
    if arv[1] == []:
        return []
    else :
        des = []
        for filho in arv[1]:
            des.append(filho[0])
            des.extend(descendentes(filho))
        return des





árvore = ( 'Rose', [ 
    ('Márcia', []), 
    ('Marília', [
        ('Bernardo', [('Jorge', [])]), 
        ('Nicole', [])
        ])
                                      ])

print(descendentes(árvore))