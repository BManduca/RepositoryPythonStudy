"""

    exemplos e aplicações da teoria de modularização

"""

import fncUteis

fncUteis.imprimiLinha2("    << MANDUCA'S SOFTWARE >>   ", 2)

fncUteis.imprimiLinha2('    << CÁLCULO DE FATORIAL >>   ', 2)

fncUteis.imprimiLinha(4)
print(fncUteis.colors[6], end='')
numb = int(input(' ==>   INSIRA UM VALOR INTEIRO: '))

ans = fncUteis.fatorial(numb)
print(f'{ans}')
print(fncUteis.colors[0], end='')
fncUteis.imprimiLinha(4)
# print(f'\n==>   O FATORIAL DE {numb} é {fat}\n')


fncUteis.imprimiLinha2(f"   << CÁLCULO DE DOBRO DE {numb} >>   ", 2)

print(fncUteis.colors[6], end='')
dobro = fncUteis.calcDobro(numb)
print(f'  >>>  O DOBRO DE {numb} ==> {dobro}')
print(fncUteis.colors[0],  end='')

