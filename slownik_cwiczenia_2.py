#Cwiczenia
#Wykorzystaj słownik do przechowywyania ulubionych liczb innych ludzi. Zapytaj
# ich o te liczby a potem pieknie wypisz.

favourite_numbers = {'Daria' : 123, 'Oskar' : 2, 'Jakub': 231}

#sorted sortuje słownik
for key, value in sorted(favourite_numbers.items()):
    print('Ulubiona liczba ' + key + ' to :' + str(value))
