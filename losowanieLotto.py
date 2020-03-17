import random

print('Witaj w kolekturze LOTTO!')
automat_liczby = []

while len(automat_liczby) < 6:
    automat = random.randint(1,49)

    if automat in automat_liczby:
        automat = random.randint(1,49)
    else:
        automat_liczby.append(automat)

wybrane_liczby = []

while len(wybrane_liczby) < 6:

    liczba = int(input('Podaj liczbę z zakresu 1 do 49\n'))

    if liczba > 49 :
        print('Błąd! Za duża liczba!')

    elif liczba < 1 :
        print('Za mała liczba!!!')

    elif liczba in wybrane_liczby:
        print('Była już taka liczba!!!')

    else:
        wybrane_liczby.append(liczba)

wygrana = [i for i in wybrane_liczby if i in automat_liczby]

print("Trafiłeś " + str(len(wygrana)) + " z liczb...")
if len(wygrana) < 3:
    print('Nic nie wygrałeś :(...')

elif len(wygrana) == 3:
    print('Brawo! Masz w kieszeni około 24 zł!')

elif len(wygrana) == 4:
    print('O kurde! Dostaniesz prawie 200 zł !!!')

elif len(wygrana) == 5:
    print('O chłopie! 5500 kasiuty przytulisz!!!')

elif len(wygrana) == 6:
    print('Rozbiłeś bank!')






