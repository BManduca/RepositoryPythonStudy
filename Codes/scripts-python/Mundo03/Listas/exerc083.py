"""
    CRIE UM PROGRAMA ONDE O USUÁRIO DIGITE UMA EXPRESSÃO
    QUALQUER QUE USE PARÊNTESES. SEU APLICATIVO DEVERÁ
    ANALISAR SE A EXPRESSÃO ESTÁ COM OS PARÊNTESES ABERTOS
    E FECHADOS NA ORDEM CORRETA.
"""
print('\n')
print('-=-'*20)
print('{:^60}'.format(' EXERCÍCIO 83 '))
print('-=-'*20)


print()
print('='*60)
expression = str(input('INSIRA UMA EXPRESSÃO ALGÉBRICA: '))
print('='*60)
print()
stack = []

for elem in expression:
    if elem == '(':
        stack.append('(')
    elif elem == ')':
        if len(expression) > 0:
            stack.pop()
        else:
            stack.append(')')
            break

if len(stack) == 0:
    print('<{:-^58}>'.format(''))
    print('{:^58}'.format('SUA EXPRESSÃO ESTÁ VÁLIDA'))
    print('<{:-^58}>'.format(''))
else:
    print('<{:-^58}>'.format(''))
    print('{:^58}'.format('SUA EXPRESSÃO ESTÁ INVÁLIDA'))
    print('<{:-^58}>'.format(''))
