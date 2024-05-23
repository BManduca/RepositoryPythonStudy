"""
  Crie um programa que realize a média das notas de um aluno através de 
  condicionais
"""

nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print('\nParabéns! Você foi aprovado!\n')
else:
    if(media == 5):
      print('\nVocê esta em recuperação! Se esforce bastante!\n')
    else:
      print('\nInfelizmente você foi reprovado!\nEstude Mais!\n')

print('Atenciosamente, a Direção!\n')