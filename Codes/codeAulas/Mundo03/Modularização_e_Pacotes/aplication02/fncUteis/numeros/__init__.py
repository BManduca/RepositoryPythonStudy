from time import sleep


def fatorial(num):
    nFat = 1
    print(f' ==>   O FATORIAL DE {num}: ', end='')
    for cont in range(num, 0, -1):
        print(cont, end='', flush=True)
        sleep(0.6)
        if cont > 1:
            print(' x ', end='')
        else:
            print(' = ', end='')
        nFat *= cont
    return nFat


def calcDobro(num):
    return num*2


def calcTriplo(num):
    return num*3
