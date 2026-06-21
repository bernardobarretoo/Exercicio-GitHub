# 5. Dada uma lista com nomes, filtrar palavras maiores que 5 letras

nomes = ['Bernardo','Clara', 'Raquel', 'Valedemar', 'Alberto', 'Guilherme', 'Fernando','Neymar', 'Anita', 'João']

maiores_que_5 = [ nome for nome in nomes if len(nome) > 5]

print(maiores_que_5)