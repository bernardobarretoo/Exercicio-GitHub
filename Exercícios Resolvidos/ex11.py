# 11. Dada uma lista com as notas de todos os alunos de uma turma, retorne a quantidade de alunos acima da média, que é 5

media = 5

notas = [3.4, 10, 6.8, 5.5, 5.0, 7.3, 1.0, 2.5, 8.9, 9.9, 9.1, 4.2, 4.9, 5.1, 9.4, 3.3]

acima_da_media = len([nota for nota in notas if nota > media])

print(acima_da_media)