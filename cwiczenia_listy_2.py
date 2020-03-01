#Cwiczenie 1
#Stwórz listę 5 miejsc, które chciałbyś odwiedzić.

places = ['Stany Zjednoczone','Szwecja','Norwegia','Finlandia','Nowa Zelandia']

#wyświetlenie listy normalnie i alfabetycznie i odwrotnie alfabetycznie
print(places)
print(sorted(places))
print(sorted((places),reverse = True))

#Cwiczenie 2
#Posortuj listę za pomocą reverse
places.reverse()
print(places)
places.reverse()
print(places)

#Cwiczenie 3
#zrób trwałe sortowanie za pomocą sort
places.sort()
print(places)
places.sort(reverse = True)
print(places)

print(len(places))