n = soma = 0

while True:
    n = int(input('Insira um número para n: '))
    if n == 999:
        break
    soma += n
# print('\nO resultado da soma é: {}'.format(soma))
print(f'\nO resultado da soma é: {soma}')
