
print('\n===== AULA 09 ======\n')

frase = 'Curso em Vídeo Python'

frase = frase.replace('Python', 'Android')

print(frase)

frase = frase.replace('Android', 'Python')

print(frase)
print('\nExiste a palavra Curso em frase?')
print('Curso' in frase)
print('\n')
print(frase.lower().find('vídeo'))
print('\n')
print(frase.split())
print('\n')
print(''.join(frase))