#cwiczenie 1 - etapy zycia
#Zapytaj o wiek a nastepnie wyswietl odpowiedni komunikat

age = int(input('Podaj swój wiek \n'))

if age < 2:
    print('Jesteś jeszcze niemowlakiem')

elif age >= 2 and age < 4:
    print('Jesteś jeszcze dzieckiem , które uczy się chodzić')

elif age >= 4 and age < 13:
    print('Jesteś dzieckiem')

elif age <= 13 and age < 20:
    print('Jesteś nastolatkiem')

elif age >= 20 and age < 65 :
    print('Jesteś dorosły')

elif age >= 65:
    print('Jesteś seniorem!')
