#Cwiczenie 1 - Lista gości
#Utwórz listę zawierającą przynajmniej 3 gości, których chciałbyś zaprosić na obiad. Następnie wykorzystaj tą listę do
# wyświetlenia dla każdej z tych osób zaproszenia.

guests = ['Jakub','Daria','Oskar']

for guest in guests:
    print(guest+' chciałbym Cię zaprosić na obiad :)')

#Dowiedziałeś się, że jedna z zaproszonych osób nie może przyjść. Wyślij nowe zaproszenia. Wyświetl, który z gości nie
#będzie mógł przyjść.

print('O, nie!' + guests[0] + ' nie będzie mógł przyjść :(\n')

#Zmodyfikuj listę i dane nowe gościa.
print('Muszę wysłać nowe zaproszenia... \n')
guests[0] = 'Igor'

#wyświetl drugi zestaw zaproszeń
for guest in guests:
    print(guest + ' chciałbym Cię zaprosić na obiad :)')

#znalazłeś nowy większy stół. Wyświetl komunikat, że masz większy stół.
print('Mam super wiadomości! Znalazłem większy stół w restauracji i mogę zaposić jeszcze kogoś :) \n')

#wstaw gościa na początku listy
guests.insert(0,'Janek')

#wstaw gościa w srodku listy
guests.insert(2,'Magda')

#wstaw gościa na końcu listy
guests.append('Joanna')

#okazuje się że aż 4 gości nie może przyjść.
guests_absent = guests[2:6]
for guest_absent in guests_absent:
    print('Niestety '+ guest_absent + ' nie może przyjść.')
print('Będzie trzeba usunąć ich z listy gości...\n')

for guests in guests[2:6]:
    guests.remove()
print(guests)


