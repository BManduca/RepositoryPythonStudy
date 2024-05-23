print('\n===== AULA 12 ======\n')

print('-'*50)

nome = str(input('\nQual é o seu nome? '))

if nome == 'Brunno':
  print('\n => Olá {}. Que nome bonito!!'.format(nome))
elif nome == 'João' or nome == 'Maria' or nome == 'Paulo':
  print('\n => Olá {}. Seu nome é bem popular no Brasil!!'.format(nome))
elif nome in 'Ana Jéssica Eduarda Carolina':
  print('\n => Olá {}. Belo nome feminino!!'.format(nome))
else:
  print('\n => Olá {}. Seu nome é diferente e bonito!!'.format(nome))
print('\n => Bom Dia!!\n')


print('-'*50)