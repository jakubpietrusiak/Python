#skrypt wypisuje rodzaje pizzy

pizza = ['margeritta', 'hawajska' , 'pepperoni','capriciosa']

for rodzaj in pizza:
    print("Lubię pizzę " + rodzaj.title())
print("Pizza to moje ulubione danie!")

#RANGE - praca na liczbach
#skrypt wypisze wszystkie liczby w zakresie 0-22
for wartosc in range(0,23):
    print(wartosc)

#skrypt wypisujący liczby powiększone o 2 w zakresie 0-10
even_numbers = list(range(2,11,2))
print(even_numbers)

#sto
sto = []

for wartosc in range(1,101):
    sto.append(wartosc)
print(sto)

#wyznaczenie najmniejszej wartosci
print(min(sto))

#wyznaczenie najwieszkej wartosci
print(max(sto))

#wyznaczenie sumy wszystkich liczb z listy
print(sum(sto))