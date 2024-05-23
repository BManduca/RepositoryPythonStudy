"""

Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo
o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos
animais seguintes foi escolhido, através das três palavras fornecidas.

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar
o animal segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.


"""

opt1 = str(input())
opt2 = str(input())
opt3 = str(input())

if opt1 == 'vertebrado':
    if opt2 == 'ave':
        if opt3 == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    elif opt2 == 'mamifero':
        if opt3 == 'onivoro':
            print('homem')
        else:
            print('vaca')
elif opt1 == 'invertebrado':
    if opt2 == 'inseto':
        if opt3 == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    elif opt2 == 'anelideo':
        if opt3 == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')



