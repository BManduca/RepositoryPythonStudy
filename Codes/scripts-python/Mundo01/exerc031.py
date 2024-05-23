"""
  DESENVOLVA PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM
  KM.
  CALCULE O PREÇO DA PASSAGEM, COBRANDO R$0,50 POR KM PARA 
  VIAGENS ATÉ 200KM E R$0,45 PARA VIAGENS MAIS LONGAS.
"""

print('{}\n===== EXERCÍCIO 31 ======\n'.format('\033[0;35m'))

print('{}-=-'.format('\033[0;33m') * 20)
print('\n\n   PROGRAMA PARA CALCULAR O VALOR DE PASSAGENS!\n\n')
print('---' * 20)
print('{}\n\nVALORES:\n'.format('\033[0;31m'))
print('\n => PARA VIAGENS ATÉ 200 Km, SÃO R$0,50 POR Km!')
print(' => PARA VIAGENS MAIS LONGAS, SÃO R$0,45 POR Km!\n')
print('-=-' * 20)
print('\n')

distViagem = float(input('Insira a distância da viagem(km): '))

if (distViagem <= 200):
  print('{}\nA sua viagem terá um total de {:.2f} km, fechando o valor da sua passagem em R${:.2f}\n'.format('\033[0;30m', distViagem, distViagem * 0.50))
else:
  print('{}\nA sua viagem terá um total de {:.2f} km.\nSendo considerada uma viagem mais longa, o valor da passagem será de R${:.2f}\n'.format('\033[0;30m', distViagem, distViagem * 0.45))