lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

total = len(lanche)

# for c in lanche:
#     print(f'lanche {c} ==> {lanche[c]}')

print('{:=^26}\n'.format(' CARDÁPIO '))

# # maneira 1 -> mostrando a posição do lanche
# for l in range(0, len(lanche)):
#     print(f'Lanche {l} ==>  {lanche[l]}')

# print('\n\n')

# # maneira 2 -> sem poder mostrar de maneira explícita a posição
# for comida in lanche:
#     print(f'{comida}')


# maneira 3 -> usando o enumerate
for pos, comida in enumerate(lanche):
    print(f'LANCHE {pos} ==> {comida}')


print(f'\n\nTOTAL DE {total} ITENS CADASTRADOS! ')

print('\nBOM APETITE!\n')

print('{:=^40}'.format(' APLICANDO SORTED '))
print(sorted(lanche))

# print(f'=> {lanche[0:]}')
# print(f'=> {lanche[:4]}')
# print(f'=> {lanche[2:]}')
# print(f'=> {lanche[-2]}')
# print(f'=> {lanche[-2:]}')
# print(f'=> {lanche[:-2]}')