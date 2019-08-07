
liczba = int(input('podaja libcze'))

flaga = True
while flaga==True:
    if liczba % 4 ==0:
        print('ok')
        flaga=False
        continue
    elif liczba % 2 ==0:
        print('git')

    elif liczba % 3 ==0:
        print('maslo')
        break