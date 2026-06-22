# 12. Crie uma lista que que extraia todas as letras das palavras e gere uma única lista. Ex: palavras = ["python", "java"]. Saída = ['p', 'y', 't', 'h', 'o', 'n', 'j', 'a', 'v', 'a']

palavras = ['motor', 'avião', 'luz']

letras = [letra for palavra in palavras for letra in palavra]

print(letras)