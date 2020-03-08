#Cwiczenie nr 1
#Utwórz program, któ©y pyta użytkownika jakiej marki samochód chciałby
# wypożyczyć, a następnie wyświetli komunikat w stylu" Chwilczkę, sprawdzam czy
# mamy takie auto"

print('Witamy w wypozyczalni aut!')
choose = input('\nJakiej marki chciałby pan auto wypożyczyć?')
print('Chwileczkę, sprawdzam czy auto marki '+choose+' mamy dostępne...')


#cwiczenie nr 2
#Utwórz program , który pyta uzytkownika na ile osób chce zarezerwoać stolik.
# Gdy odpowiedz jest wieksza niz 6 , wyswietl komunikat ze nie ma takiego

table = int(input('\nNa ile osob chce pan zarezerwowac stolik?'))
if table >= 6:
    print('Nie mamy tak dużych stolików...')
else:
    print('Super. Mamy coś odpowiedniego!')

#Cwiczenie nr 3
#Popros o liczbe i sprawdz czy to wielokrotnosc liczby 10

number = int(input('\nPodaj jakąś liczbę : '))
if number % 10 == 0:
    print('Liczba jest wielokrotnością liczby 10 !')
else:
    print('Nie jest to wielokrotność 10')