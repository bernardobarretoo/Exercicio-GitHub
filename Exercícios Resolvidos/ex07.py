# 7. Gere uma lista contendo o tamanho de cada palavra. Ex de entrada: ["python", "java", "javascript", "c"]

palavras = list(input('Escreva as palavras separadas por espaço: ').split())
tamanho = [len(palavra) for palavra in palavras]
print(tamanho)