

person1 = {'imie' : 'Daria', 'nazwisko' : 'Pietrusiak'}
person2 = {'imie' : 'Oskar', 'nazwisko' : 'Pietrusiak'}
person3 = {'imie' : 'Jakub', 'nazwisko' : 'Pietrusiak'}
persons = [person1,person2,person3]

for person in persons:
    print(person)

print('Całkowita liczba osób w słowniku to ' + str(len(persons)))