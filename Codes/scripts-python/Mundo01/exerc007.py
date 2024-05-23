"""
    Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""

print('===== EXERCÍCIO 07 ======\n')

nota1 = float(input('Insira a primeira nota do aluno: '))
nota2 = float(input('Insira a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

print('A média entre {} e {} é igual a {:.1f}'.format(nota1, nota2, media))