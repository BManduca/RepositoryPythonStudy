"""
  DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO
  DE TRÊS RETAS E DIGA AO USUÁRIO SE ELAS PODEM OU NÃO 
  FORMAR UM TRIÂNGULO
"""

cores = {'limpa':'\033[m', 'azul':'\033[34m','brancoevermelho':'\033[7;31;40m', 'azuleamarelo':'\033[7;33;44m'}

print('\n===== EXERCÍCIO 35 ======\n')

print('{}-={}'.format(cores['azuleamarelo'], cores['limpa']) * 20)
print('\n   ANALISADOR DE TRIÂNGULOS\n')
print('{}-={}'.format(cores['brancoevermelho'], cores['limpa']) * 20)

print('\n')

comp1 = float(input('Insira o comprimento da primeira reta: '))
comp2 = float(input('Insira o comprimento da segunda reta: '))
comp3 = float(input('Insira o comprimento da terceira reta: '))

if (comp1 + comp2 > comp3) and (comp1 + comp3 > comp2) and (comp2 + comp3 > comp1):
    print('\nOs comprimentos de reta {}, {} e {} formam um triângulo!\n'.format(comp1, comp2, comp3))
else:
    print('\nOs comprimentos de reta {}, {} e {} não formam um triângulo!\n'.format(comp1, comp2, comp3))