"""

    exemplos e aplicações da teoria de modularização

"""

from fncUteis import numeros, strings

strings.imprimiLinha2("    << MANDUCA'S SOFTWARE >>   ", 2)

strings.imprimiLinha2('    << CÁLCULO DE FATORIAL >>   ', 2)

strings.imprimiLinha(4)
print(strings.colors[6], end='')
numb = int(input(' ==>   INSIRA UM VALOR INTEIRO: '))

ans = numeros.fatorial(numb)
print(f'{ans}')
print(strings.colors[0], end='')
strings.imprimiLinha(4)
# print(f'\n==>   O FATORIAL DE {numb} é {fat}\n')


strings.imprimiLinha2(f"   << CÁLCULO DE DOBRO DE {numb} >>   ", 2)

print(strings.colors[6], end='')
dobro = numeros.calcDobro(numb)
print(f'  >>>  O DOBRO DE {numb} ==> {dobro}')
print(strings.colors[0],  end='')

