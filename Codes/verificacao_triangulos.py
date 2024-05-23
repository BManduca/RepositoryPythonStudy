#codigo para realizar a verificação de triângulos

a = float(input('Insira o primeiro lado: '))
b = float(input('Insira o segundo lado: '))
c = float(input('Insira o terceiro lado: '))

#testando se inicialmente é um triângulo
if(a + b < c) or (a + c < b) or (b + c < a) : 
  print('Não é um triângulo!!')
elif (a == b) and (a == c) :
  print('Triângulo Equilatero!')
elif (a == b) or (a == c) or (b == c) : 
  print('Triângulo Isósceles!!')
else: 
  print('Triângulo Escaleno!!')