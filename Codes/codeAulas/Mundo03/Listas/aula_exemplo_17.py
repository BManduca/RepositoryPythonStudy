num = [7, 2, 5, 8]

num[2] = 6

num.append(9)

num.insert(1, 10)

if 10 in num:
    num.remove(10)
else:
    print('não foi encontrado o valor solicitado.')

print(f'Lista original -> {num}')

num.sort()

print(f'Lista ordenada -> {num}')

num.pop()

num.sort(reverse=True)

print(f'Lista ordenada inversamente -> {num}')
print(f'Essa lista tem {len(num)} elementos')

# print('-'*40)

# valores = []

# # valores.append(10)
# # valores.append(5)
# # valores.append(2)
# # valores.append(0)

# for val in range(0, 4):
#     valores.append(int(input('INSIRA UM VALOR: ')))

# print('\nNOVA LISTA: \n')

# for c, v in enumerate(valores):
#     print(f'| {c} => {v:2} |')
# print('\nFINAL DA LISTA!\n')
print('-'*40)


a = [8, 2, 6, 1]
b = a
b[2] = 12

print(f'Lista a: {a}')
print(f'\nLista b: {b}')

print('-'*40)