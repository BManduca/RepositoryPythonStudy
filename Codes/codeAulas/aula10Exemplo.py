"""
  Crie um programa que avalie o tempo de uso do seu carro e mostre uma 
  mensagem de acordo com a avaliação
"""

tempoCarro = int(input("Quantos anos tem seu carro? "))
if tempoCarro <= 3:
    print("\nCarro novo!")
else:
    print("\nCarro velho")
print("--FIM--\n")


"""
condição simplificada

tempoCarro = int(input("Quantos anos tem seu carro? "))
print('\ncarro novo'if tempoCarro <= 3 else '\ncarro velho')
print('--FIM--\n')

"""